import sys

from PyQt4 import QtGui
from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker

from core.api import renderOptions
from core.buckets import BucketOrderInfo, BucketOrderSortType
from application import Application
from core.parallel import ThreadPool


my_renderer = None
my_scene = None
my_camera = None
my_buckets_info = None

def load_from_file(filename):
    from loader.pbrt_loader import PbrtLoader
    from loader.pbrt.pbrtLexer import pbrtLexer
    from loader.pbrt.pbrtParser import pbrtParser

    input = FileStream(filename)
    lexer = pbrtLexer(input)
    tokens = CommonTokenStream(lexer)
    loader = pbrtParser(tokens)
    tree = loader.body()
    printer = PbrtLoader()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)

def render(multiThreaded: bool = True):
    global my_renderer
    global my_scene
    global my_camera
    global my_buckets_info
    my_renderer.render(my_scene, BucketOrderInfo(BucketOrderSortType.Hilbert, 30, 30), multiThreaded)


def main():
    global my_renderer
    global my_scene
    global my_camera

#    load_from_file("scenes/ao_02.pbrt")
#    load_from_file("scenes/ao_01.pbrt")
#    load_from_file("scenes/debug.pbrt")
#    load_from_file("scenes/cornell.pbrt")

#    load_from_file("scenes/cornellebox_pathtracing_lq.pbrt")
#    load_from_file("scenes/cornellebox_pathtracing_mq.pbrt")
    load_from_file("scenes/cornellebox_pathtracing_jensen_lq.pbrt")

    my_renderer = renderOptions.make_renderer()
    my_scene = renderOptions.make_scene()

    qt_app = QtGui.QApplication(sys.argv)
    app = Application(my_renderer.camera.film)

    pool = ThreadPool(1)
    pool.add_task(render)
#    render(False)

    sys.exit(qt_app.exec_())


if __name__ == '__main__':
    main()
