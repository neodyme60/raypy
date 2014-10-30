import string
from core.camera_sample import CameraSample
from core.film import Film
from core.param_set import ParamSet
from core.projective_camera import ProjectiveCamera
from maths.config import infinity_max_f
from maths.point3d import Point3d
from maths.vector3d import Vector3d
from core.transform import Transform
from core.ray import Ray


class OrthographicCamera(ProjectiveCamera):

    def __init__(self, cam2world: Transform, screen_window: [float]*4, shutter_open: float, shutter_close: float, lensr: float, focald: float, fov: float, film: Film):

        super().__init__(cam2world, Transform.create_orthographic(0.0, 1.0), screen_window, shutter_open, shutter_close, lensr, focald, film)
        self.dxCamera = (Point3d(1.0, 0.0 ,0.0) * self.rasterToCamera) - (Point3d(0.0, 0.0, 0.0) * self.rasterToCamera)
        self.dyCamera = (Point3d(0.0, 1.0 ,0.0) * self.rasterToCamera) - (Point3d(0.0, 0.0, 0.0) * self.rasterToCamera)

    def generate_ray(self, sample:CameraSample)->Ray:

        point_camera = Point3d(sample.image_xy[0], sample.image_xy[1], 0.0) * self.rasterToCamera
        direction = Vector3d(0.0, 0.0, 1.0)

        r = Ray(point_camera, direction, 0.0, infinity_max_f)

        if self.lensRadius>0.0:
            pass
            #todo

        r.time = sample.time
        return r * self.camera_to_world