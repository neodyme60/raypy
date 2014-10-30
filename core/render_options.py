from core.api import make_filter, make_film, make_camera, make_accelerator, make_sampler, make_surface_integrator, \
    make_volume_integrator
from core.camera import Camera
from core.param_set import ParamSet
from core.renderer import Renderer
from core.scene import Scene
from core.transform import Transform
from core.volume_region import AggregateVolume
from renderers.sampler_renderer import AmbientOcclusionRenderer


class RenderOptions():

    def __init__(self):
        self.filterName = None
        self.filterParams = ParamSet()
        self.filmName = None
        self.filmParams = ParamSet()
        self.samplerName = None
        self.samplerParams = ParamSet()
        self.acceleratorName = None
        self.acceleratorParams = ParamSet()
        self.rendererName = None
        self.rendererParams = ParamSet()
        self.surfIntegratorName = None
        self.surfIntegratorParams = ParamSet()
        self.volIntegratorName = None
        self.volIntegratorParams = ParamSet()
        self.cameraName = None
        self.cameraParams = ParamSet()
        self.primitives = []
        self.instances = []
        self.cameraToWorld = Transform.create_identity()
        self.volumeRegions = []
        self.lights = []


    def make_camera(self)->Camera:
        filter = make_filter(self.filterName, self.filterParams)
        film = make_film(self.filmName, self.filmParams, filter)
        camera = make_camera(self.cameraName, self.cameraParams, self.cameraToWorld, film)
        return camera

    def make_scene(self)->Scene:

        volume_region = None
        if len(self.volumeRegions)  == 0:
            volume_region = None
        elif len(self.volumeRegions) == 1:
            volume_region = self.volumeRegions[0]
        volume_region = AggregateVolume(self.volumeRegions)

        accelerator = make_accelerator(self.acceleratorName, self.primitives, self.acceleratorParams)
        if accelerator == None:
            accelerator = make_accelerator("bvh", self.primitives, ParamSet())


        scene = Scene(accelerator, self.lights, volume_region)
#    // Erase primitives, lights, and volume regions from _RenderOptions_
#    primitives.erase(primitives.begin(), primitives.end());
#    lights.erase(lights.begin(), lights.end());
#    volumeRegions.erase(volumeRegions.begin(), volumeRegions.end());

        return scene

    def make_renderer(self)->Renderer:
        renderer = None
        camera = self.make_camera()
        if self.rendererName == "sampler":
            sampler = make_sampler(self.samplerName, self.samplerParams, camera.film, camera)
            surface_integrator = make_surface_integrator(self.surfIntegratorName, self.surfIntegratorParams)
            volume_integrator = make_volume_integrator(self.volIntegratorName, self.volIntegratorParams)
            render = AmbientOcclusionRenderer(sampler, camera, surface_integrator, volume_integrator)

        return renderer

    def __init__(self, sampler: Sampler, camera: Camera, samples_count: int=1, max_distance: float=infinity_max_f):
        super().__init__()

