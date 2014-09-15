from core.camera_sample import CameraSample
from core.ray import Ray
from core.film import Film

class Camera:

    def __init__(self, cam2world:float, shutterOpen:float, sutterClose:float, film:Film):
        self.film = film
        self.camera_to_world = cam2world
        self.shutterOpen = shutterOpen
        self.sutterClose = sutterClose

    def GenerateRay(self, sample:CameraSample, r: Ray):
        pass
