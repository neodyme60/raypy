from copy import copy
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
from core.integrator import SurfaceIntegrator, VolumeIntegrator
from core.light import Light
from core.material import Material
from core.param_set import ParamSet
from core.primitive import Primitive
from core.render_options import RenderOptions
from core.shape import Shape
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

renderOptions = RenderOptions()
curTransform = Transform.create_identity()
namedCoordinateSystems = {}
pushedActiveTransformBits = []
pushedTransforms = []

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
        paramset.find_point("P"),
        paramset.find_ints("indices"),
        None, None
        )
    return shape

def create_shape_plan(paramset: ParamSet, object2world: Transform, world2object: Transform) -> Plane:
    shape = Plane(object2world, world2object)
    return shape

def create_light_point(paramset: ParamSet, light2world: Transform) -> PointLight:
    return None

def create_surface_integrator_ambient_occlusion(paramset: ParamSet) -> AmbientOcclusionIntegrator:
    samples_count = paramset.find_int("nsamples", 2048)
    max_distance = paramset.find_float("maxdist", infinity_max_f)
    integrator = AmbientOcclusionIntegrator(samples_count, max_distance)
    return integrator

def create_surface_integrator_direct_lighting(paramset: ParamSet) -> DirectLightingIntegrator:
    return None

def create_aggregator_bvh(primitives: [Primitive], paramset: ParamSet) -> BoundingIntervalHierarchy:
    return None

def create_aggregator_kdtree(primitives: [Primitive], paramset: ParamSet) -> KDTree:
    return None

def create_aggregator_grid(primitives: [Primitive], paramset: ParamSet) -> UniformGrid:
    refine_immediately = paramset.find_bool("refineimmediately", False)
    grid = UniformGrid(primitives, refine_immediately)
    return grid

def create_aggregator_simple(primitives: [Primitive], paramset: ParamSet) -> Simple:
    return Simple(primitives)

def create_sampler_random(paramset: ParamSet, film: Film, camera: Camera) -> RandomSampler:
    sampler = RandomSampler(BucketExtend(0, 0, film.width - 1, film.height - 1), 1)
    return sampler

def create_sampler_stratified(paramset: ParamSet, film: Film, camera: Camera) -> StratifiedSampler:
    return None

def create_sampler_lowdiscrepancy(paramset: ParamSet, film: Film, camera: Camera) -> LowDiscrepancySampler:
    return None

def create_sampler_halton(paramset: ParamSet, film: Film, camera: Camera) -> HaltonSampler:
    return None

def create_sampler_bestcandidate(paramset: ParamSet, film: Film, camera: Camera) -> BestcandidateSampler:
    return None

def create_sampler_adaptive(paramset: ParamSet, film: Film, camera: Camera) -> AdaptiveSampler:
    return None

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

def create_film_image(paramset: ParamSet, filter: Filter) -> Film:
    w = paramset.find_int("xresolution", 640)
    h = paramset.find_int("yresolution", 480)
    return Film(w, h)

def create_material_matte(materialToWorld: Transform, paramset: ParamSet) -> MatteMaterial:
    return None

def create_material_mirror(materialToWorld: Transform, paramset: ParamSet) -> MirrorMaterial:
    return None

def make_material(name: string, materialToWorld: Transform, paramset: ParamSet) -> Material:
    material = None
    if name == "matte":
        material = create_material_matte(materialToWorld, paramset)
    elif name == "mirror":
        material = create_material_mirror(materialToWorld, paramset)
    return material

def make_film(name: string, paramset: ParamSet, filter: Filter) -> Film:
    film = None
    if name == "image":
        film = create_film_image(paramset, filter)
    return film

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

def make_volume_integrator(name: string, paramset: ParamSet) -> VolumeIntegrator:
    integrator = None
    return integrator

def make_shape(name: string, paramset: ParamSet, object2world: Transform, world2object: Transform) -> Shape:
    shape = None
    if name == "sphere":
        shape = create_shape_sphere(paramset, object2world, world2object)
    if name == "trianglemesh":
        shape = create_shape_triangle_mesh(paramset, object2world, world2object)
    if name == "plane":
        shape = create_shape_plan(paramset, object2world, world2object)
    return shape

def make_light(name: string, paramset: ParamSet, light2world: Transform) -> Light:
    light = None
    if name == "point":
        light = create_light_point(paramset, light2world)
    return light

def make_surface_integrator(name: string, paramset: ParamSet) -> SurfaceIntegrator:
    integrator = None
    if name == "ambientocclusion":
        integrator = create_surface_integrator_ambient_occlusion(paramset)
    elif name == "directlighting":
        integrator = create_surface_integrator_direct_lighting(paramset)
    return integrator

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

def make_camera(name: string, paramset: ParamSet, cam2world: Transform, film: Film) -> Camera:
    camera = None
    if name == "perspective":
        camera = create_perspective_camera(paramset, cam2world, film)
    elif name == "orthographic":
        camera = create_orthographic_camera(paramset, cam2world, film)
    elif name == "environment":
        camera = create_environment_camera(paramset, cam2world, film)
    return camera

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

def pbrtIdentity():
    global  curTransform
    curTransform = Transform.create_identity()

def pbrtTranslate(dx: float, dy: float, dz: float):
    global  curTransform
    curTransform = curTransform * Transform.create_translate(dx, dy, dz)

def pbrtRotate(angle: float, ax: float, ay: float, az: float):
    global  curTransform
    curTransform = curTransform * Transform.create_rotate(angle, Vector3d(ax, ay, az))

def pbrtScale(sx: float, sy: float, sz: float):
    global  curTransform
    curTransform = curTransform * Transform.create_scale(sx, sy, sz)

def pbrtLookAt(e: Vector3d, l: Vector3d, u: Vector3d):
    global  curTransform
    curTransform = curTransform * Transform.create_look_at(e, l, u)

def pbrtConcatTransform(transform:[float] * 16):
    pass

def pbrtTransform(transform:[float] * 16):
    pass

def pbrtCoordinateSystem(name: string):
    global  curTransform
    namedCoordinateSystems[name] = curTransform

def pbrtCoordSysTransform(name: string):
    global  curTransform
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
    renderOptions.filmParams = copy(params)

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
    renderOptions.cameraToWorld = curTransform

def pbrtWorldBegin():
    pass

def pbrtAttributeBegin():
    global pushedTransforms
    global curTransform
    pushedTransforms.append(curTransform)

def pbrtAttributeEnd():
    global pushedTransforms
    global curTransform
    curTransform = pushedTransforms.pop()

def pbrtTransformBegin():
    pass

def pbrtTransformEnd():
    pass

def pbrtTexture(name:string,  params:ParamSet):
    pass

def pbrtMaterial(name:string, params:ParamSet):
    pass

def pbrtMakeNamedMaterial(name:string, params:ParamSet):
    pass

def pbrtNamedMaterial(name:string):
    pass

def pbrtLightSource(name:string, params:ParamSet):
    pass

def pbrtAreaLightSource(name:string, params: ParamSet):
    pass

def pbrtShape(name:string, params:ParamSet):
    shape = make_shape(name, params, curTransform, curTransform.get_invert() )
    renderOptions.primitives.append(shape)

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
