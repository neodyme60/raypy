from camera.orthographic_camera import OrthographicCamera
from camera.perspective_camera import PerspectiveCamera
from core.buckets import BucketOrderInfo, BucketOrderSortType, BucketExtend
from core.film import Film
from core.scene import Scene
from renderers.bounding_volume_renderer import BoundingVolumeRenderer
from samplers.randomSampler import RandomSampler
from shapes.sphere import Sphere
from application import Application
from core.transform import Transform
from PyQt4 import QtCore, QtGui
import sys
from core.parallel import ThreadPool

my_renderer = None
my_scene = None
my_camera = None
my_buckets_info = None


def load_scene(w:int, h:int):
    global my_renderer
    global my_scene
    global my_camera
    global my_buckets_info

    # create scene populate with object
    my_scene = Scene()
    transform = Transform.create_translate(0.0, 0.0, 50.0)
    form1 = Sphere(transform, transform.get_invert(), 0.02)
    my_scene.add_geometry(form1)

    shutter_open = 0.0
    shutter_close = 0.0
    nb_samples = 1

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

    my_camera = PerspectiveCamera(Transform.create_translate(0.0, 0.0, 0.0), screen_window, 0.0, 1.0, 5.0, 1.0, 90.0, my_film)
#    my_camera = OrthographicCamera(Transform.create_translate(0.0, 0.0, -5.0), screen_window, 0.0, 1.0, 5.0, 1.0, 60.0, my_film)

    #sampler
    my_sampler = RandomSampler(BucketExtend(0, 0, w - 1, h - 1), nb_samples, shutter_open, shutter_close)

    #buket
    my_buckets_info = BucketOrderInfo(BucketOrderSortType.Random, 50, 50)

    #create renderer and assign scene
    my_renderer = BoundingVolumeRenderer(my_sampler, my_camera)


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

    width = 300
    height = 300

    load_scene(width, height)

    qt_app = QtGui.QApplication(sys.argv)
    app = Application(width, height, my_camera.film)

    pool = ThreadPool(20)
    pool.add_task(render)
    # render()

    sys.exit(qt_app.exec_())


if __name__ == '__main__':
    main()
