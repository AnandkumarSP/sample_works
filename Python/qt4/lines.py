from PyQt4.QtGui import QWidget, QPolygonF, QPainter, QPen, QBrush, QColor, \
    QApplication, QIcon, QVBoxLayout, QSlider, QHBoxLayout, QPushButton, QLCDNumber
from PyQt4.QtCore import QObject, SIGNAL, SLOT, QPointF, Qt, QRectF, QPointF
import time, sys

#================================================================
# For the next block I used this post
# http://stackoverflow.com/a/3220819/736306, 
# but I wish to replace it with self.liniar_bez(),
# biliniar_bez(), self.cubic_bez() and self.fourG_bez()
# because I want to control 't' with self.slider

def avg(a, b):
  xa, ya = a
  xb, yb = b
  return (xa + xb) * 0.5, (ya + yb) * 0.5

def bez4split(p0, p1, p2, p3, p4):
    p01 = avg(p0, p1)
    p12 = avg(p1, p2)
    p23 = avg(p2, p3)
    p34 = avg(p3, p4)
    p012 = avg(p01, p12)
    p123 = avg(p12, p23)
    p234 = avg(p23, p34)
    p0123 = avg(p012, p123)
    p1234 = avg(p123, p234)
    p01234 = avg(p0123, p1234)
    return [(p0, p01, p012, p0123, p01234),
        (p01234, p1234, p234, p34, p4)]

def bez4(p0, p1, p2, p3, p4, levels=5):
    if levels <= 0:
        return [p0, p4]
    else:
        (a0, a1, a2, a3, a4), (b0, b1, b2, b3, b4) = bez4split(p0, p1, p2, p3, p4)
        return (bez4(a0, a1, a2, a3, a4, levels - 1) +
                bez4(b0, b1, b2, b3, b4, levels - 1)[1:])
#================================================================

points = [[160, 75], [115, 567], [292, 58], [685, 194], [734, 517]]
coords = bez4(*points)

class Bezier(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.lcd = QLCDNumber(self)
        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.setRange(0, 100)
        self.closeButton = QPushButton('Close')

        bottomLayout = QHBoxLayout()
        bottomLayout.addWidget(self.lcd)
        bottomLayout.addWidget(self.slider)
        bottomLayout.addWidget(self.closeButton)

        mainLayout = QVBoxLayout()
        mainLayout.addStretch(1)
        mainLayout.addLayout(bottomLayout)

        self.setLayout(mainLayout)

        self.time = 0
        self.time_step = 0.025
        self.timer_id = self.startTimer(1)

        self.tracking = None

        QObject.connect(self.closeButton, SIGNAL('clicked(bool)'), app.exit)
        QObject.connect(self.slider, SIGNAL('valueChanged(int)'), self.lcd, SLOT('display(float)'))
        #self.slider.valueChanged.connect(self.lcd.display)

        self.setWindowTitle('Bonus Example')

    def poly(self, pts):
        return QPolygonF(map(lambda p: QPointF(*p), pts))

    def bezAnimation(self):
        painter = QPainter(self)
        painter.setRenderHints(QPainter.Antialiasing)

        pts = points[:]
        crds = coords[:]

        painter.setPen(QPen(QColor(Qt.lightGray), 3, Qt.DashDotDotLine))
        painter.drawPolyline(self.poly(pts))

        painter.setBrush(QBrush(QColor(255, 025, 0)))
        painter.setPen(QPen(QColor(Qt.lightGray), 1))
        for x, y in pts:
            painter.drawEllipse(QRectF(x - 4, y - 4, 8, 8))

    def paintEvent(self, event):
        self.bezAnimation()

    # As you know, 0.00 > 't' > 1.00
    # and QSlider does not provide support for float numbers,
    # so we simply divide t by 100
    def liniar_bez(self, p, t):
        t = t / 100.0
        new_p[0] = (1 - t) * p[0][0] + t * p[1][0]
        new_p[1] = (1 - t) * p[0][1] + t * p[1][1]

    def biliniar_bez(self, p, t):
        t = t / 100.0
        new_p[0][0] = ((1 - t) ** 2) * p[0][0] + 2 * (1 - t) * t * p[1][0] + (t ** 2) * p[2][0]
        new_p[0][1] = ((1 - t) ** 2) * p[0][1] + 2 * (1 - t) * t * p[1][1] + (t ** 2) * p[2][1]

    def cubic_bez(self, p, t):
        t = t / 100.0
        new_p[0][0] = ((1 - t) ** 3) * p[0][0] + 3 * ((1 - t) ** 2) * t * p[1][0] + (t ** 2) * p[2][0] + (t ** 3) * p[3][0]
        new_p[0][1] = ((1 - t) ** 3) * p[0][1] + 3 * ((1 - t) ** 2) * t * p[1][1] + (t ** 2) * p[2][1] + (t ** 3) * p[3][1]

    def fourG_bez(self, p, t):
        t = t / 100.0
        new_p[0][0] = ((1 - t) ** 4) * p[0][0] + 4 * ((1 - t) ** 3) * t * p[1][0] + 4 * (1 - t) * (t ** 2) * p[2][0] + 4 * (1 - t) * (t ** 3) * p[3][0] + (t ** 4) * p[4][0]
        new_p[0][1] = ((1 - t) ** 4) * p[0][1] + 4 * ((1 - t) ** 3) * t * p[1][1] + 4 * (1 - t) * (t ** 2) * p[2][1] + 4 * (1 - t) * (t ** 3) * p[3][1] + (t ** 4) * p[4][1]

    def timerEvent(self, event):
        if self.timer_id == event.timerId():
            #self.bezAnimation()
            self.time += self.time_step
            self.update()

    def closeEvent(self, event):
        self.deleteLater()

    #================================================================
    # And this one too
    # http://stackoverflow.com/a/3220819/736306
    def mousePressEvent(self, event):
        i = min(range(len(points)),
            key=lambda i: (event.x() - points[i][0]) ** 2 +
                      (event.y() - points[i][1]) ** 2)

        self.tracking = lambda p: points.__setitem__(i, p)

    def mouseMoveEvent(self, event):
       if self.tracking:
            self.tracking((event.x(), event.y()))
            self.update()

    def mouseReleaseEvent(self, event):
        self.tracking = None
    #================================================================

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Bezier()
    form.setGeometry(10, 30, 871, 727)
    form.show()
    sys.exit(app.exec_())
