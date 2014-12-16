from copy import copy, deepcopy
import string

from aggregates.bvh import BoundingIntervalHierarchy
from aggregates.kd_tree import KDTree
from aggregates.simple import Simple
from aggregates.uniform_grid import UniformGrid
from camera.environment_camera import EnvironmentCamera
from camera.orthographic_camera import OrthographicCamera
from camera.perspective_camera import PerspectiveCamera
from core.buckets import BucketExtend
from core.camera import Camera
from core.film import Film
from core.filter import Filter
from core.geometric_primitive import GeometricPrimitive
from core.graphics_state import GraphicsState
from core.light import Light, AreaLight
from core.material import Material
from core.param_set import ParamSet
from core.primitive import Primitive
from core.spectrum import Spectrum
from core.texture import Texture
from core.texture_param_set import TextureParamSet
from lights.diffuse_area_light import DiffuseAreaLight
from lights.projection_light import ProjectionLight
from lights.spot_ligt import SpotLight
from maths.point3d import Point3d
from renderers.render_options import RenderOptions
from core.shape import Shape
from core.surface_integrator import SurfaceIntegrator
from core.volume_integrator import VolumeIntegrator
from lights.point_light import PointLight
from core.sampler import Sampler
from core.transform import Transform
from materials.matte_material import MatteMaterial
from materials.mirror_material import MirrorMaterial
from maths.config import infinity_max_f
from maths.vector3d import Vector3d
from samplers.adaptiveSampler import AdaptiveSampler
from samplers.bestcandidateSampler import BestcandidateSampler
from samplers.haltonSampler import HaltonSampler
from samplers.lowdiscrepancySampler import LowDiscrepancySampler
from samplers.randomSampler import RandomSampler
from samplers.stratifiedSampler import StratifiedSampler
from shapes.plane import Plane
from shapes.sphere import Sphere
from shapes.triangle import TriangleMesh
from surface_integrator.ambient_occlusion_integrator import AmbientOcclusionIntegrator
from surface_integrator.direct_lighting_integrator import DirectLightingIntegrator
from surface_integrator.path import PathIntegrator
from textures.constant_texture import ConstantTexture


renderOptions = RenderOptions()
curTransform = [Transform.create_identity()]
namedCoordinateSystems = {}
pushedActiveTransformBits = []
pushedTransforms = []
graphicsState = GraphicsState()
pushedGraphicsStates = [GraphicsState()]


# ==========================camera
def create_environment_camera(paramset: ParamSet, cam2world: Transform, film: Film) -> EnvironmentCamera:
    return None


def create_perspective_camera(paramset: ParamSet, cam2world: Transform, film: Film) -> PerspectiveCamera:
    shutteropen = paramset.find_float("shutteropen", 0.0)
    shutterclose = paramset.find_float("shutterclose", 1.0)
    if shutterclose < shutteropen:
        shutterclose, shutteropen = shutteropen, shutterclose
    lensradius = paramset.find_float("lensradius", 0.0)
    focaldistance = paramset.find_float("focaldistance", 1e30)
    frame = paramset.find_float("frameaspectratio", float(film.width) / float(film.height))
    fov = paramset.find_float("fov", 90.0)
    halffov = paramset.find_float("halffov", -1.0)
    if halffov > 0.0:
        # hack for structure synth, which exports half of the full fov
        fov = 2.0 * halffov

    screen_window = [float] * 4
    if frame > 1.0:
        screen_window[0] = -frame
        screen_window[1] = frame
        screen_window[2] = -1.0
        screen_window[3] = 1.0
    else:
        screen_window[0] = -1.0
        screen_window[1] = 1.0
        screen_window[2] = -1.0 / frame
        screen_window[3] = 1.0 / frame

    camera = PerspectiveCamera(cam2world, screen_window, shutteropen, shutterclose, lensradius, focaldistance, fov,
                               film)
    return camera


def create_orthographic_camera(paramset: ParamSet, cam2world: Transform, film: Film) -> OrthographicCamera:
    return None


def make_camera(name: string, paramset: ParamSet, cam2world: Transform, film: Film) -> Camera:
    camera = None
    if name == "perspective":
        camera = create_perspective_camera(paramset, cam2world, film)
    elif name == "orthographic":
        camera = create_orthographic_camera(paramset, cam2world, film)
    elif name == "environment":
        camera = create_environment_camera(paramset, cam2world, film)
    return camera


#==========================shape

def create_shape_sphere(paramset: ParamSet, object2world: Transform, world2object: Transform) -> Sphere:
    radius = paramset.find_float("radius", 1.0)
    zmin = paramset.find_float("zmin", -radius)
    zmax = paramset.find_float("zmax", radius)
    phimax = paramset.find_float("phimax", 360.0)
    shape = Sphere(object2world, world2object, radius, zmin, zmax, phimax)
    return shape


def create_shape_triangle_mesh(paramset: ParamSet, object2world: Transform, world2object: Transform) -> TriangleMesh:
    shape = TriangleMesh(
        object2world,
        world2object,
        paramset.find_points("P"),
        paramset.find_ints("indices"),
        None, None
    )
    return shape


def create_shape_plan(paramset: ParamSet, object2world: Transform, world2object: Transform) -> Plane:
    shape = Plane(object2world, world2object)
    return shape


def make_shape(name: string, paramset: ParamSet, object2world: Transform, world2object: Transform) -> Shape:
    shape = None
    if name == "sphere":
        shape = create_shape_sphere(paramset, object2world, world2object)
    elif name == "trianglemesh":
        shape = create_shape_triangle_mesh(paramset, object2world, world2object)
    elif name == "plane":
        shape = create_shape_plan(paramset, object2world, world2object)
    return shape


#==========================light

def create_light_point(paramSet: ParamSet, light2world: Transform) -> PointLight:
    I = paramSet.find_spectrum("I", Spectrum(1.0))
    sc = paramSet.find_spectrum("scale", Spectrum(1.0))
    P = paramSet.find_point("from", Point3d(0.0, 0.0, 0.0))
    l2w = Transform.create_translate(P.x, P.y, P.z) * light2world
    return PointLight(l2w, I * sc)


def create_spotLight(paramSet: ParamSet, light2world: Transform) -> PointLight:
    from maths.matrix44 import Matrix44
    from maths.vector4d import Vector4d

    I = paramSet.find_spectrum("I", Spectrum(1.0))
    sc = paramSet.find_spectrum("scale", Spectrum(1.0))
    coneangle = paramSet.find_float("coneangle", 30.0)
    conedelta = paramSet.find_float("conedeltaangle", 5.0)

    # Compute spotlight world to light transformation
    frome = paramSet.find_point("from", Point3d(0.0, 0.0, 0.0))
    to = paramSet.find_point("to", Point3d(0.0, 0.0, 1.0))
    dir = (to - frome).get_normalized()
    du, dv = Transform.create_coordinateSystem(dir)
    m = Matrix44.create_from_vector4d(
        Vector4d(du.x, du.y, du.z, 0.0),
        Vector4d(dv.x, dv.y, dv.z, 0.0),
        Vector4d(dir.x, dir.y, dir.z, 0.0),
        Vector4d(0.0, 0.0, 0.0, 1.0))
    dirToZ = Transform(m)
    light2world = light2world * Transform.create_translate(frome.ex, frome.ey, frome.ez) * dirToZ.get_invert()
    return SpotLight(light2world, I * sc, coneangle, coneangle - conedelta)


def create_goniometric_light(paramset: ParamSet, light2world: Transform) -> PointLight:
    return None


def create_projection_light(paramSet: ParamSet, light2world: Transform) -> PointLight:
    I = paramSet.find_spectrum("I", Spectrum(1.0))
    sc = paramSet.find_spectrum("scale", Spectrum(1.0))
    fov = paramSet.find_float("fov", 45.)
    texname = paramSet.find_filename("mapname", "")
    return ProjectionLight(light2world, I * sc, texname, fov)


def create_distant_light(paramset: ParamSet, light2world: Transform) -> PointLight:
    return None


def create_infinite_light(paramset: ParamSet, light2world: Transform) -> PointLight:
    return None


def make_light(name: string, light2world: Transform, paramset: ParamSet) -> Light:
    light = None
    if name == "point":
        light = create_light_point(paramset, light2world)
    elif name == "spot":
        light = create_spotLight(paramset, light2world)
    elif name == "goniometric":
        light = create_goniometric_light(paramset, light2world)
    elif name == "projection":
        light = create_projection_light(paramset, light2world)
    elif name == "distant":
        light = create_distant_light(paramset, light2world)
    elif name == "infinite" or name == "exinfinite":
        light = create_infinite_light(paramset, light2world)
    return light


#==========================surface integrator

def create_surface_integrator_ambient_occlusion(paramset: ParamSet) -> AmbientOcclusionIntegrator:
    samples_count = paramset.find_int("nsamples", 2048)
    max_distance = paramset.find_float("maxdist", infinity_max_f)
    integrator = AmbientOcclusionIntegrator(samples_count, max_distance)
    return integrator


def create_surface_integrator_direct_lighting(paramset: ParamSet) -> DirectLightingIntegrator:
    samples_count = paramset.find_int("nsamples", 2048)
    max_distance = paramset.find_float("maxdist", infinity_max_f)
    #todo depth etc
    integrator = DirectLightingIntegrator(samples_count, max_distance)
    return integrator

def create_surface_integrator_path(paramset: ParamSet) -> DirectLightingIntegrator:
    samples_count = paramset.find_int("maxdepth", 2)
    integrator = PathIntegrator(samples_count)
    return integrator

def make_surface_integrator(name: string, paramset: ParamSet) -> SurfaceIntegrator:
    integrator = None
    if name == "ambientocclusion":
        integrator = create_surface_integrator_ambient_occlusion(paramset)
    elif name == "directlighting":
        integrator = create_surface_integrator_direct_lighting(paramset)
    elif name == "path":
        integrator = create_surface_integrator_path(paramset)
    return integrator


#==========================aggregator

def create_aggregator_bvh(primitives: [Primitive], paramset: ParamSet) -> BoundingIntervalHierarchy:
    return None


def create_aggregator_kdtree(primitives: [Primitive], paramset: ParamSet) -> KDTree:
    return None


def create_aggregator_grid(primitives: [Primitive], paramset: ParamSet) -> UniformGrid:
    refine_immediately = paramset.find_bool("refineimmediately", True)
    grid = UniformGrid(primitives, refine_immediately)
    return grid


def create_aggregator_simple(primitives: [Primitive], paramset: ParamSet) -> Simple:
    return Simple(primitives)


def make_accelerator(name: string, primitives: [Primitive], paramset: ParamSet) -> Primitive:
    accelerator = None
    if name == "bvh":
        accelerator = create_aggregator_bvh(primitives, paramset)
    elif name == "grid":
        accelerator = create_aggregator_grid(primitives, paramset)
    elif name == "kdtree":
        accelerator = create_aggregator_kdtree(primitives, paramset)
    elif name == "simple":
        accelerator = create_aggregator_simple(primitives, paramset)
    return accelerator


#==========================sampler

def create_sampler_random(paramset: ParamSet, film: Film, camera: Camera) -> RandomSampler:
    samples = paramset.find_int("pixelsamples", 1)
    sampler = RandomSampler(BucketExtend(0, 0, film.width - 1, film.height - 1), samples, camera.shutterOpen,
                            camera.shutterClose)
    return sampler


def create_sampler_stratified(paramset: ParamSet, film: Film, camera: Camera) -> StratifiedSampler:
    jitter = paramset.find_bool("jitter", True)
    xsamples = paramset.find_int("xsamples", 2)
    ysamples = paramset.find_int("ysamples", 2)
    sampler = StratifiedSampler(BucketExtend(0, 0, film.width - 1, film.height - 1), xsamples, ysamples, jitter,
                                camera.shutterOpen, camera.shutterClose)
    return sampler


def create_sampler_lowdiscrepancy(paramset: ParamSet, film: Film, camera: Camera) -> LowDiscrepancySampler:
    sampler = LowDiscrepancySampler(BucketExtend(0, 0, film.width - 1, film.height - 1), 1, camera.shutterOpen,
                                    camera.shutterClose)
    return sampler


def create_sampler_halton(paramset: ParamSet, film: Film, camera: Camera) -> HaltonSampler:
    sampler = HaltonSampler(BucketExtend(0, 0, film.width - 1, film.height - 1), 1, camera.shutterOpen,
                            camera.shutterClose)
    return sampler


def create_sampler_bestcandidate(paramset: ParamSet, film: Film, camera: Camera) -> BestcandidateSampler:
    sampler = BestcandidateSampler(BucketExtend(0, 0, film.width - 1, film.height - 1), 1, camera.shutterOpen,
                                   camera.shutterClose)
    return sampler


def create_sampler_adaptive(paramset: ParamSet, film: Film, camera: Camera) -> AdaptiveSampler:
    sampler = AdaptiveSampler(BucketExtend(0, 0, film.width - 1, film.height - 1), 1, camera.shutterOpen,
                              camera.shutterClose)
    return sampler


def make_sampler(name: string, paramset: ParamSet, film: Film, camera: Camera) -> Sampler:
    sampler = None
    if name == "random":
        sampler = create_sampler_random(paramset, film, camera)
    elif name == "stratified":
        sampler = create_sampler_stratified(paramset, film, camera)
    elif name == "lowdiscrepancy":
        sampler = create_sampler_lowdiscrepancy(paramset, film, camera)
    elif name == "halton":
        sampler = create_sampler_halton(paramset, film, camera)
    elif name == "bestcandidate":
        sampler = create_sampler_bestcandidate(paramset, film, camera)
    elif name == "adaptive":
        sampler = create_sampler_adaptive(paramset, film, camera)
    return sampler


#==========================filter

def create_filter_box(paramset: ParamSet) -> Filter:
    return None


def create_filter_gaussian(paramset: ParamSet) -> Filter:
    return None


def create_filter_mitchell(paramset: ParamSet) -> Filter:
    return None


def create_filter_sinc(paramset: ParamSet) -> Filter:
    return None


def create_filter_triangle(paramset: ParamSet) -> Filter:
    return None


def make_filter(name: string, paramset: ParamSet) -> Filter:
    filter = None
    if name == "box":
        filter = create_filter_box(paramset)
    elif name == "gaussian":
        filter = create_filter_gaussian(paramset)
    elif name == "mitchell":
        filter = create_filter_mitchell(paramset)
    elif name == "sinc":
        filter = create_filter_sinc(paramset)
    elif name == "triangle":
        filter = create_filter_triangle(paramset)
    return filter


#==========================spectrum texture

def CreateConstantSpectrumTexture(tex2world: Transform, tp: TextureParamSet):
    return ConstantTexture(tp.FindFloat("value", 1.0))


def CreateScaleSpectrumTexture(tex2world: Transform, tp: TextureParamSet):
    pass


def CreateMixSpectrumTexture(tex2world: Transform, tp: TextureParamSet):
    pass


def CreateBilerpSpectrumTexture(tex2world: Transform, tp: TextureParamSet):
    pass


def CreateImageSpectrumTexture(tex2world: Transform, tp: TextureParamSet):
    pass


def CreateUVSpectrumTexture(tex2world: Transform, tp: TextureParamSet):
    pass


def CreateCheckerboardSpectrumTexture(tex2world: Transform, tp: TextureParamSet):
    pass


def CreateDotsSpectrumTexture(tex2world: Transform, tp: TextureParamSet):
    pass


def CreateFBmSpectrumTexture(tex2world: Transform, tp: TextureParamSet):
    pass


def CreateWrinkledSpectrumTexture(tex2world: Transform, tp: TextureParamSet):
    pass


def CreateMarbleSpectrumTexture(tex2world: Transform, tp: TextureParamSet):
    pass


def CreateWindySpectrumTexture(tex2world: Transform, tp: TextureParamSet):
    pass


def make_spectrum_texture(name: string, tex2world: Transform, tp: TextureParamSet):
    texture = None
    if name == "constant":
        texture = CreateConstantSpectrumTexture(tex2world, tp)
    elif name == "scale":
        texture = CreateScaleSpectrumTexture(tex2world, tp)
    elif name == "mix":
        texture = CreateMixSpectrumTexture(tex2world, tp)
    elif name == "bilerp":
        texture = CreateBilerpSpectrumTexture(tex2world, tp)
    elif name == "imagemap":
        texture = CreateImageSpectrumTexture(tex2world, tp)
    elif name == "uv":
        texture = CreateUVSpectrumTexture(tex2world, tp)
    elif name == "checkerboard":
        texture = CreateCheckerboardSpectrumTexture(tex2world, tp)
    elif name == "dots":
        texture = CreateDotsSpectrumTexture(tex2world, tp)
    elif name == "fbm":
        texture = CreateFBmSpectrumTexture(tex2world, tp)
    elif name == "wrinkled":
        texture = CreateWrinkledSpectrumTexture(tex2world, tp)
    elif name == "marble":
        texture = CreateMarbleSpectrumTexture(tex2world, tp)
    elif name == "windy":
        texture = CreateWindySpectrumTexture(tex2world, tp)
    return ConstantTexture(tp.FindSpectrum("value", Spectrum(1.0)))


#==========================float texture

def create_constant_float_texture(tex2world: Transform, tp: TextureParamSet):
    return ConstantTexture(tp.FindFloat("value", 1.0))


def CreateScaleFloatTexture(tex2world: Transform, tp: TextureParamSet):
    pass


def CreateMixFloatTexture(tex2world: Transform, tp: TextureParamSet):
    pass


def CreateBilerpFloatTexture(tex2world: Transform, tp: TextureParamSet):
    pass


def CreateImageFloatTexture(tex2world: Transform, tp: TextureParamSet):
    pass


def CreateUVFloatTexture(tex2world: Transform, tp: TextureParamSet):
    pass


def CreateCheckerboardFloatTexture(tex2world: Transform, tp: TextureParamSet):
    pass


def CreateDotsFloatTexture(tex2world: Transform, tp: TextureParamSet):
    pass


def CreateFBmFloatTexture(tex2world: Transform, tp: TextureParamSet):
    pass


def CreateWrinkledFloatTexture(tex2world: Transform, tp: TextureParamSet):
    pass


def CreateMarbleFloatTexture(tex2world: Transform, tp: TextureParamSet):
    pass


def CreateWindyFloatTexture(tex2world: Transform, tp: TextureParamSet):
    pass


def make_float_texture(name: string, tex2world: Transform, paramset: TextureParamSet) -> Texture:
    texture = None
    if name == "constant":
        texture = create_constant_float_texture(tex2world, paramset)
    elif name == "scale":
        texture = CreateScaleFloatTexture(tex2world, paramset)
    elif name == "mix":
        texture = CreateMixFloatTexture(tex2world, paramset)
    elif name == "bilerp":
        texture = CreateBilerpFloatTexture(tex2world, paramset)
    elif name == "imagemap":
        texture = CreateImageFloatTexture(tex2world, paramset)
    elif name == "uv":
        texture = CreateUVFloatTexture(tex2world, paramset)
    elif name == "checkerboard":
        texture = CreateCheckerboardFloatTexture(tex2world, paramset)
    elif name == "dots":
        texture = CreateDotsFloatTexture(tex2world, paramset)
    elif name == "fbm":
        texture = CreateFBmFloatTexture(tex2world, paramset)
    elif name == "wrinkled":
        texture = CreateWrinkledFloatTexture(tex2world, paramset)
    elif name == "marble":
        texture = CreateMarbleFloatTexture(tex2world, paramset)
    elif name == "windy":
        texture = CreateWindyFloatTexture(tex2world, paramset)
    else:
        raise Exception("float texture not found")
    return texture


#==========================material

def create_material_matte(materialToWorld: Transform, paramset: TextureParamSet) -> MatteMaterial:
    Kd = paramset.GetSpectrumTexture("Kd", Spectrum(0.50))
    sigma = paramset.GetFloatTexture("sigma", 0.0)
    bumpMap = paramset.GetFloatTextureOrNull("bumpmap")
    return MatteMaterial(Kd, sigma, bumpMap)


def create_material_mirror(materialToWorld: Transform, paramset: TextureParamSet) -> MirrorMaterial:
    return None


def make_material(name: string, materialToWorld: Transform, paramset: TextureParamSet) -> Material:
    material = None
    if name == "matte":
        material = create_material_matte(materialToWorld, paramset)
    elif name == "mirror":
        material = create_material_mirror(materialToWorld, paramset)
    return material


#==========================film

def create_film_image(paramset: ParamSet, filter: Filter) -> Film:
    w = paramset.find_int("xresolution", 640)
    h = paramset.find_int("yresolution", 480)
    return Film(w, h)


def make_film(name: string, paramset: ParamSet, filter: Filter) -> Film:
    film = None
    if name == "image":
        film = create_film_image(paramset, filter)
    return film


#==========================volume integrator

def make_volume_integrator(name: string, paramset: ParamSet) -> VolumeIntegrator:
    integrator = None
    return integrator


#==========================area light source

def create_diffuse_area_light(light2world: Transform, paramSet: ParamSet, shape: Shape):
    L = paramSet.find_spectrum("L", Spectrum(1.0))
    sc = paramSet.find_spectrum("scale", Spectrum(1.0))
    nSamples = paramSet.find_int("nsamples", 1)
    #    if renderOptions.quickRender:
    #        nSamples = max(1, nSamples / 4)
    return DiffuseAreaLight(light2world, L * sc, nSamples, shape)


def make_area_light(name: string, light2world: Transform, paramSet: ParamSet, shape: Shape) -> AreaLight:
    area = None
    if name == "area" or name == "diffuse":
        area = create_diffuse_area_light(light2world, paramSet, shape)
    else:
        raise Exception("Area light unknown")
    #        Warning("Area light \"%s\" unknown.", name.c_str());
    #    paramSet.ReportUnused();
    return area


#=================================================================================================================

def pbrtIdentity():
    global curTransform
    for i in range(len(curTransform)):
        curTransform[i] = Transform.create_identity()


def pbrtTranslate(dx: float, dy: float, dz: float):
    global curTransform
    for i in range(len(curTransform)):
        curTransform[i] = curTransform[i] * Transform.create_translate(dx, dy, dz)


def pbrtRotate(angle: float, ax: float, ay: float, az: float):
    global curTransform
    for i in range(len(curTransform)):
        curTransform[i] = curTransform[i] * Transform.create_rotate(angle, Vector3d(ax, ay, az))


def pbrtScale(sx: float, sy: float, sz: float):
    global curTransform
    for i in range(len(curTransform)):
        curTransform[i] = curTransform[i] * Transform.create_scale(sx, sy, sz)


def pbrtLookAt(e: Vector3d, l: Vector3d, u: Vector3d):
    global curTransform
    for i in range(len(curTransform)):
        curTransform[i] = curTransform[i] * Transform.create_look_at(e, l, u)


def pbrtConcatTransform(transform:[float] * 16):
    pass


def pbrtTransform(transform:[float] * 16):
    pass


def pbrtCoordinateSystem(name: string):
    global curTransform
    namedCoordinateSystems[name] = curTransform


def pbrtCoordSysTransform(name: string):
    global curTransform
    if namedCoordinateSystems[name]:
        curTransform = namedCoordinateSystems[name]


def pbrtActiveTransformAll():
    pass


def pbrtActiveTransformEndTime():
    pass


def pbrtActiveTransformStartTime():
    pass


def pbrtTransformTimes(start:float, end:float):
    pass


def pbrtPixelFilter(name:string, params:ParamSet):
    renderOptions.filterName = name
    renderOptions.filterParams = copy(params)


def pbrtFilm(name:string, params:ParamSet):
    renderOptions.filmName = name
    renderOptions.filmParams = copy(params)


def pbrtSampler(name:string, params: ParamSet):
    renderOptions.samplerName = name
    renderOptions.samplerParams = copy(params)


def pbrtAccelerator(name: string, params:ParamSet):
    renderOptions.acceleratorName = name
    renderOptions.acceleratorParams = copy(params)


def pbrtSurfaceIntegrator(name:string, params:ParamSet):
    renderOptions.surfIntegratorName = name
    renderOptions.surfIntegratorParams = copy(params)


def pbrtVolumeIntegrator(name:string, params:ParamSet):
    renderOptions.volIntegratorName = name
    renderOptions.volIntegratorParams = copy(params)


def pbrtRenderer(name:string, params:ParamSet):
    renderOptions.rendererName = name
    renderOptions.rendererParams = copy(params)


def pbrtCamera(name:string, params:ParamSet):
    renderOptions.cameraName = name
    renderOptions.cameraParams = copy(params)
    renderOptions.cameraToWorld = curTransform[0]


def pbrtWorldBegin():
    global curTransform
    for i in range(len(curTransform)):
        curTransform[i] = Transform.create_identity()


def pbrtAttributeBegin():
    global pushedTransforms
    global curTransform
    pushedTransforms.append(deepcopy(curTransform))
    pushedGraphicsStates.append(deepcopy(graphicsState))


def pbrtAttributeEnd():
    global pushedTransforms
    global curTransform
    global graphicsState
    curTransform = pushedTransforms.pop()
    graphicsState = pushedGraphicsStates.pop()


def pbrtTransformBegin():
    global pushedTransforms
    global curTransform
    pushedTransforms.append(deepcopy(curTransform))


def pbrtTransformEnd():
    global pushedTransforms
    global curTransform
    curTransform = pushedTransforms.pop()


def pbrtTexture(name:string, type: string, texname:string, params:ParamSet):
    global graphicsState

    tp = TextureParamSet(params, params, graphicsState.floatTextures, graphicsState.spectrumTextures)

    if type == "float":
        if texname in graphicsState.floatTextures:
            raise Exception("texture already defined")
        ft = make_float_texture(texname, curTransform[0], tp)
        if ft:
            graphicsState.floatTextures[name] = ft
    elif type == "color" or type == "spectrum":
        if texname in graphicsState.spectrumTextures:
            raise Exception("texture already defined")
        st = make_spectrum_texture(texname, curTransform[0], tp)
        if st:
            graphicsState.spectrumTextures[name] = st
    else:
        pass


def pbrtMaterial(name:string, params:ParamSet):
    global graphicsState
    graphicsState.material = name
    graphicsState.materialParams = deepcopy(params)
    graphicsState.currentNamedMaterial = ""


def pbrtMakeNamedMaterial(name:string, params:ParamSet):
    global graphicsState
    mp = TextureParamSet(params, graphicsState.materialParams, graphicsState.floatTextures,
                         graphicsState.spectrumTextures)
    matName = mp.FindString("type")
    if matName == None:
        raise Exception("No parameter string \"type\" found in MakeNamedMaterial")
    else:
        mtl = make_material(matName, curTransform[0], mp)
        if mtl:
            graphicsState.namedMaterials[name] = mtl


def pbrtNamedMaterial(name:string):
    global graphicsState
    graphicsState.currentNamedMaterial = name


def pbrtLightSource(name:string, params:ParamSet):
    l = make_light(name, curTransform[0], params)
    if l:
        renderOptions.lights.append(l)
    else:
        raise Exception("pbrtLightSource: light type \"%s\" unknown.", name)


def pbrtAreaLightSource(name:string, params: ParamSet):
    global graphicsState
    graphicsState.areaLight = name
    graphicsState.areaLightParams = deepcopy(params)

def pbrtShape(name:string, params:ParamSet):
    global graphicsState

    shape = make_shape(name, params, curTransform[0], curTransform[0].get_invert())

    mat = graphicsState.CreateMaterial(params)

    areaLight = None
    if graphicsState.areaLight != "":
        areaLight = make_area_light(graphicsState.areaLight, curTransform[0], graphicsState.areaLightParams, shape)

    geom_prim = GeometricPrimitive(shape, mat, areaLight)

    renderOptions.primitives.append(geom_prim)
    if areaLight is not None:
        renderOptions.lights.append(areaLight)


def pbrtReverseOrientation():
    pass


def pbrtVolume(name:string, params:ParamSet):
    pass


def pbrtObjectBegin(name:string):
    pass


def pbrtObjectEnd():
    pass


def pbrtObjectInstance(name:string):
    pass


def pbrtWorldEnd():
    pass
