from core.projective_camera import ProjectiveCamera
from core.transform import Transform
from maths.point3d import Point3d
from core.film import Film
from core.camera_sample import CameraSample
from core.ray import Ray
from maths.config import infinity_max_f, infinity_min_f
from maths.vector3d import Vector3d


class PerspectiveCamera(ProjectiveCamera):

    def __init__(self, cam2world: Transform, screen_window: [float]*4, shutter_open: float, shutter_close: float, lensr: float, focald: float, fov: float, film: Film):

        super().__init__(cam2world, Transform.create_perspective(fov, infinity_min_f, 1000.0), screen_window, shutter_open, shutter_close, lensr, focald, film)
        self.dxCamera = (Point3d(1.0, 0.0 ,0.0) * self.rasterToCamera) - (Point3d(0.0, 0.0, 0.0) * self.rasterToCamera)
        self.dyCamera = (Point3d(0.0, 1.0 ,0.0) * self.rasterToCamera) - (Point3d(0.0, 0.0, 0.0) * self.rasterToCamera)

    def generate_ray(self, sample:CameraSample)->Ray:

        camera_point = Point3d(sample.image_xy[0], sample.image_xy[1], 0.0) * self.rasterToCamera
        camera_direction = Vector3d(camera_point.x, camera_point.y, camera_point.z).get_normalized()

        r = Ray(camera_point, camera_direction, 0.0, infinity_max_f)

        if self.lensRadius>0.0:
            pass
            #todo

        r.time = sample.time
        return r * self.camera_to_world