from core.projective_camera import ProjectiveCamera
from core.transform import Transform
from maths.point3d import Point3d
from core.film import Film
from core.camera_sample import CameraSample
from core.ray import Ray
from maths.config import infinity_max_f

class PerspectiveCamera(ProjectiveCamera):

    def __init__(self, cam2world: Transform, sopen: float, sclose: float, lensr: float, focald: float, fov: float, film: Film):
        ProjectiveCamera.__init__(self, cam2world, Transform.create_perspective(fov, 1e-2, 1000.0), sopen, sclose, lensr, focald, film)
        self.dxCamera = (Point3d(1.0, 0.0 ,0.0) * self.rasterToCamera) - (Point3d(0.0, 0.0, 0.0) * self.rasterToCamera)
        self.dyCamera = (Point3d(0.0, 1.0 ,0.0) * self.rasterToCamera) - (Point3d(0.0, 0.0, 0.0) * self.rasterToCamera)

    def GenerateRay(self, sample:CameraSample, r: Ray):
        point_camera = Point3d(sample.image_x, sample.image_y, 0.0) * self.rasterToCamera()
        r = Ray(Point3d(0.0, 0.0, 0.0), point_camera, 0.0, infinity_max_f)
        return r * self.camera_to_world