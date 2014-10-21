import sys
from PyQt4 import QtGui
from camera.perspective_camera import PerspectiveCamera
from core.buckets import BucketOrderInfo, BucketOrderSortType, BucketExtend
from core.film import Film
from core.scene import Scene
from integrator.ambient_occlusion_integrator import AmbientOcclusionIntegrator
from maths.vector3d import Vector3d
from renderers.ambient_occlusion_renderer import AmbientOcclusionRenderer
from samplers.randomSampler import RandomSampler
from shapes.plane import Plane
from shapes.sphere import Sphere
from application import Application
from core.transform import Transform
from core.parallel import ThreadPool


my_renderer = None
my_scene = None
my_camera = None
my_buckets_info = None


class Plan(object):
    pass


def load_scene(w:int, h:int):
    global my_renderer
    global my_scene
    global my_camera
    global my_buckets_info

    surface_integrator = AmbientOcclusionIntegrator(10, 10.0)

    # create scene populate with object
    my_scene = Scene(surface_integrator)

    transform = Transform.create_translate(0.0, 2.0, 0.0)
    form1 = Sphere(transform, transform.get_invert(), 2.0)

#    transform2 = Transform.create_rot_x(0)*Transform.create_translate(0.0, 0.0, 5.0)
    transform2 = Transform.create_identity()
    form2 = Plane(transform2,transform2.get_invert())

    my_scene.add_geometry(form1)
    my_scene.add_geometry(form2)

    shutter_open = 0.0
    shutter_close = 0.0
    nb_samples = 5

    # film
    my_film = Film(w, h)

    #camera
    frame = my_film.width / my_film.height
    screen_window = [float] * 4
    if frame > 1.0:
        screen_window[0] = -frame
        screen_window[1] = frame
        screen_window[2] = -1.0
        screen_window[3] = 1.0
    else:
        screen_window[0] = -1.0
        screen_window[1] = 1.0
        screen_window[2] = -1.0 / frame
        screen_window[3] = 1.0 / frame

    transform3 = Transform.create_look_at(Vector3d(0.0, 2.0, -5.0), Vector3d(0.0, 0.0, 0.0), Vector3d.get_up())
    my_camera = PerspectiveCamera(transform3, screen_window, 0.0, 1.0, 5.0, 1.0, 60.0, my_film)
#    my_camera = OrthographicCamera(Transform.create_translate(0.0, 0.0, 0.0), screen_window, 0.0, 1.0, 5.0, 1.0, 60.0, my_film)

    #sampler
    my_sampler = RandomSampler(BucketExtend(0, 0, w - 1, h - 1), 1, shutter_open, shutter_close)
#    my_sampler = StratifiedSampler(BucketExtend(0, 0, w - 1, h - 1), 1, 1, True, shutter_open, shutter_close)
#    my_sampler = HaltonSampler(BucketExtend(0, 0, w - 1, h - 1), 5, shutter_open, shutter_close)

    #buket
    my_buckets_info = BucketOrderInfo(BucketOrderSortType.Hilbert, 10, 10 )

    #create renderer and assign scene
    my_renderer = AmbientOcclusionRenderer(my_sampler, my_camera)
#    my_renderer = BoundingVolumeRenderer(my_sampler, my_camera)


def render():
    global my_renderer
    global my_scene
    global my_camera
    global my_buckets_info
    my_renderer.render(my_scene, my_buckets_info)


def main():
    global my_renderer
    global my_scene
    global my_camera

    width = 200
    height = 200

    load_scene(width, height)

    qt_app = QtGui.QApplication(sys.argv)
    app = Application(width, height, my_camera.film)

    pool = ThreadPool(1)
    pool.add_task(render)
#    render()

    sys.exit(qt_app.exec_())


if __name__ == '__main__':
    main()
