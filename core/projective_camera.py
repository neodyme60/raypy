from core.camera import Camera
from core.camera_sample import CameraSample
from core.ray import Ray
from core.film import Film
from core.transform import Transform


class ProjectiveCamera(Camera):

    def __init__(self, cam2world: Transform, proj: Transform, sopen: float, sclose: float, lensr: float, focald: float, film: Film):
        Camera.__init__(self, cam2world, sopen, sclose, film)
        self.cameraToScreen = proj
        self.screenToRaster = Transform.create_scale(film.width, film.height, 1.0)
        self.rasterToScreen = Transform.get_invert(self.screenToRaster)
        self.rasterToCamera = Transform.get_invert(self.cameraToScreen) * self.rasterToScreen
        self.lensRadius = lensr
        self.focalDistance= focald

    def GenerateRay(self, sample:CameraSample, r: Ray):
        pass

