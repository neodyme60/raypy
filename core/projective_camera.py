from core.camera import Camera
from core.camera_sample import CameraSample
from core.ray import Ray
from core.film import Film
from core.transform import Transform


class ProjectiveCamera(Camera):

    def __init__(self, cam2world: Transform, projection_matrix: Transform, screen_window: [float]*4, shutter_open: float, shutter_close: float, lensr: float, focald: float, film: Film):
        super().__init__(cam2world, shutter_open, shutter_close, film)
        self.cameraToScreen = projection_matrix
        self.screenToRaster = \
                              Transform.create_translate(-screen_window[0], -screen_window[3], 0.0) * \
                              Transform.create_scale(1.0 / (screen_window[1] - screen_window[0]), 1.0 / (screen_window[2] - screen_window[3]), 1.0) * \
                              Transform.create_scale(film.width, film.height, 1.0)
        self.rasterToScreen = Transform.get_invert(self.screenToRaster)
        self.rasterToCamera = self.rasterToScreen * Transform.get_invert(self.cameraToScreen)
        self.lensRadius = lensr
        self.focalDistance= focald

    def generate_ray(self, sample:CameraSample, r: Ray):
        pass

