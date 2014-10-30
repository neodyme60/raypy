import string

from aggregates.bvh import BoundingIntervalHierarchy
from aggregates.kd_tree import KDTree
from aggregates.simple import Simple
from aggregates.uniform_grid import UniformGrid
from camera.environment_camera import EnvironmentCamera
from camera.orthographic_camera import OrthographicCamera
from camera.perspective_camera import PerspectiveCamera
from core.camera import Camera
from core.film import Film
from core.filter import Filter
from core.integrator import SurfaceIntegrator, VolumeIntegrator
from core.light import Light
from core.material import Material
from core.param_set import ParamSet
from core.primitive import Primitive
from core.shape import Shape
from lights.point_light import PointLight
from core.render_options import RenderOptions
from core.sampler import Sampler
from core.transform import Transform
from materials.matte_material import MatteMaterial
from materials.mirror_material import MirrorMaterial
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


class Options():
    def __init__(self):
        pass


def create_environment_camera(paramset: ParamSet, cam2world: Transform) -> EnvironmentCamera:
    return None


def create_perspective_camera(paramset: ParamSet, cam2world: Transform) -> PerspectiveCamera:
    return None


def create_orthographic_camera(paramset: ParamSet, cam2world: Transform) -> OrthographicCamera:
    return None


def create_shape_sphere(paramset: ParamSet, object2world: Transform, world2object: Transform) -> Sphere:
    return None


def create_shape_triangle_mesh(paramset: ParamSet, object2world: Transform, world2object: Transform) -> TriangleMesh:
    return None


def create_shape_plan(paramset: ParamSet, object2world: Transform, world2object: Transform) -> Plane:
    return None


def create_light_point(paramset: ParamSet, light2world: Transform) -> PointLight:
    return None


def create_surface_integrator_ambient_occlusion(paramset: ParamSet) -> AmbientOcclusionIntegrator:
    return None


def create_surface_integrator_direct_lighting(paramset: ParamSet) -> DirectLightingIntegrator:
    return None


def create_aggregator_bvh(primitives: [Primitive], paramset: ParamSet) -> BoundingIntervalHierarchy:
    return None


def create_aggregator_kdtree(primitives: [Primitive], paramset: ParamSet) -> KDTree:
    return None


def create_aggregator_grid(primitives: [Primitive], paramset: ParamSet) -> UniformGrid:
    return None


def create_aggregator_simple(primitives: [Primitive], paramset: ParamSet) -> Simple:
    return None


def create_sampler_random(paramset: ParamSet, film: Film, camera: Camera) -> RandomSampler:
    return None


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
    return None


def create_material_matte(materialToWorld: Transform, paramset: ParamSet) - >MatteMaterial:
    return None


def create_material_mirror(materialToWorld: Transform, paramset: ParamSet) - >MirrorMaterial:
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
        create_filter_box(paramset)
    elif name == "gaussian":
        create_filter_gaussian(paramset)
    elif name == "mitchell":
        create_filter_mitchell(paramset)
    elif name == "sinc":
        create_filter_sinc(paramset)
    elif name == "triangle":
        create_filter_triangle(paramset)
    return filter


def make_volume_integrator(name: string, paramset: ParamSet) -> VolumeIntegrator:
    integrator = None
    return integrator


def make_shape(name: string, paramset: ParamSet, object2world: Transform, world2object: Transform, film: Film) -> Shape:
    shape = None
    if name == "sphere":
        create_shape_sphere(paramset, object2world, world2object)
    if name == "trianglemesh":
        create_shape_triangle_mesh(paramset, object2world, world2object)
    if name == "plan":
        create_shape_plan(paramset, object2world, world2object)
    return shape


def make_light(name: string, paramset: ParamSet, light2world: Transform, film: Film) -> Light:
    light = None
    if name == "point":
        create_light_point(paramset, light2world)
    return light


def make_surface_integrator(name: string, paramset: ParamSet) -> SurfaceIntegrator:
    integrator = None
    if name == "ambientocclusion":
        create_surface_integrator_ambient_occlusion(paramset)
    elif name == "directlighting":
        create_surface_integrator_direct_lighting(paramset)
    return integrator


def make_accelerator(name: string, primitives: [Primitive], paramset: ParamSet) -> Primitive:
    accelerator = None
    if name == "bvh":
        create_aggregator_bvh(primitives, paramset)
    elif name == "grid":
        create_aggregator_grid(primitives, paramset)
    elif name == "kdtree":
        create_aggregator_kdtree(primitives, paramset)
    elif name == "sample":
        create_aggregator_simple(primitives, paramset)
    return accelerator


def make_camera(name: string, paramset: ParamSet, cam2world: Transform, film: Film) -> Camera:
    camera = None
    if name == "perspective":
        create_perspective_camera(paramset, cam2world)
    elif name == "orthographic":
        create_orthographic_camera(paramset, cam2world)
    elif name == "environment":
        create_environment_camera(paramset, cam2world)
    return camera


def make_sampler(name: string, paramset: ParamSet, film: Film, camera: Camera) -> Sampler:
    sampler = None
    if name == "random":
        create_sampler_random(paramset, film, camera)
    elif name == "stratified":
        create_sampler_stratified(paramset, film, camera)
    elif name == "lowdiscrepancy":
        create_sampler_lowdiscrepancy(paramset, film, camera)
    elif name == "halton":
        create_sampler_halton(paramset, film, camera)
    elif name == "bestcandidate":
        create_sampler_bestcandidate(paramset, film, camera)
    elif name == "adaptive":
        create_sampler_adaptive(paramset, film, camera)
    return sampler


def pbrtInit(option: Options):
    pass


def pbrtCleanup():
    pass


def pbrtIdentity():
    pass


def pbrtTranslate(dx: float, dy:float, dz:float):
    global curTransform
    curTransform = curTransform * Transform.create_translate(dx, dy, dz)


def pbrtRotate(angle:float, ax:float, ay:float, az:float):
    global curTransform
    curTransform = curTransform * Transform.create_rotate(angle, Vector3d(ax, ay, az))


def pbrtScale(sx:float, sy:float, sz:float):
    global curTransform
    curTransform = curTransform * Transform.create_scale(sx, sy, sz)


def pbrtLookAt(ex:float, ey:float, ez:float,
               lx:float, ly:float, lz:float,
               ux:float, uy:float, uz:float):
    global curTransform
    curTransform = curTransform * Transform.create_look_at(Vector3d(ex, ey, ez), Vector3d(lx, ly, lz),
                                                           Vector3d(ux, uy, uz))


def pbrtConcatTransform(transform:[float] * 16):
    pass


def pbrtTransform(transform:[float] * 16):
    pass


def pbrtCoordinateSystem(str:string):
    pass


def pbrtCoordSysTransform(str:string):
    pass


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
    renderOptions.filmParams = params


def pbrtFilm(name:string, params:ParamSet):
    renderOptions.filmName = name
    renderOptions.filmParams = params


def pbrtSampler(name:string, params: ParamSet):
    renderOptions.samplerName = name
    renderOptions.samplerParams = params


def pbrtAccelerator(name: string, params:ParamSet):
    renderOptions.acceleratorName = name
    renderOptions.acceleratorParams = params


def pbrtSurfaceIntegrator(name:string, params:ParamSet):
    renderOptions.surfIntegratorName = name
    renderOptions.surfIntegratorParams = params


def pbrtVolumeIntegrator(name:string, params:ParamSet):
    renderOptions.volIntegratorName = name
    renderOptions.volIntegratorParams = params


def pbrtRenderer(name:string, params:ParamSet):
    renderOptions.rendererName = name
    renderOptions.rendererParams = params


def pbrtCamera(name:string, params:ParamSet):
    renderOptions.cameraName = name
    renderOptions.cameraParams = params


def pbrtWorldBegin():
    pass


def pbrtAttributeBegin():
    pass


def pbrtAttributeEnd():
    pass


def pbrtTransformBegin():
    pass


def pbrtTransformEnd():
    pass


def pbrtTexture(name:string, type:string, texname:string, params:ParamSet):
    pass


def pbrtMaterial(name:string, params:ParamSet):
    pass


def pbrtMakeNamedMaterial(name:string, params:ParamSet):
    pass


def pbrtNamedMaterial(name:string):
    pass


def pbrtLightSource(name:string, params:ParamSet):
    pass


def pbrtAreaLightSource(name:string, params:ParamSet):
    pass


def pbrtShape(name:string, params:ParamSet):
    pass


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
