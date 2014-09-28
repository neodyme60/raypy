from PyQt4 import QtCore, QtGui
import numpy
import array
from core.film import Film


class Application(QtGui.QMainWindow):
    def __init__(self, w: int, h: int, film: Film):
        super(Application, self).__init__()
        self.w = w
        self.h = h
        self.i = 0
        self.film = film
        self.initUI()

    def updateData(self):
        self.qimage = QtGui.QImage(self.film.data, self.w, self.h, QtGui.QImage.Format_RGB32)
        self.pix = QtGui.QPixmap.fromImage(self.qimage)
#        self.myScaledPixmap = self.pix.scaled(self.imageLabel.size(), QtCore.Qt.KeepAspectRatio)
        self.imageLabel.setPixmap(self.pix)
        self.i += 1

    def initUI(self):
        self.statusBar().showMessage('Ready')

        self.imageLabel = QtGui.QLabel('Zetcode', self)
        self.imageLabel.setGeometry(QtCore.QRect(0, 0, self.w, self.h))
        self.imageLabel.setBackgroundRole(QtGui.QPalette.Base)
        self.imageLabel.setSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        self.imageLabel.setScaledContents(True)

        # SET UP RECURRING EVENTS
        self.timer = QtCore.QTimer()
        self.timer.start(0.2)
        self.connect(self.timer, QtCore.SIGNAL('timeout()'), self.updateData)

        self.setGeometry(300, 300, self.w, self.h)
        self.setWindowTitle('Absolute')
        self.show()
