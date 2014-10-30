import string
from core.camera import Camera
from core.film import Film
from core.param_set import ParamSet
from core.transform import Transform


class EnvironmentCamera(Camera):

    def __init__(self, cam2world: Transform, screen_window: [float] * 4, shutter_open: float, shutter_close: float,
                 lensr: float, focald: float, fov: float, film: Film):
        super().__init__(cam2world, shutter_open, shutter_close, film)

    #todo