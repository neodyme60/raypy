from core.camera_sample import CameraSample
from core.ray import Ray
from core.film import Film
from core.transform import Transform


class Camera:
    def __init__(self, cam2world: Transform, shutter_open: float, shutter_close: float, film:Film):
        self.film = film
        self.camera_to_world = cam2world
        self.shutterOpen = shutter_open
        self.shutterClose = shutter_close

    def generate_ray(self, sample:CameraSample):
        raise NotImplemented
