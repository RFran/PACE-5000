#------- IMPORTS -------#

from PyQt4 import QtCore, QtGui
import sys
import pyqtgraph as pg

#------- TESTS -------#
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


#------- WINDOW -------#

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        MainWindow.setObjectName(_fromUtf8("MainWindow"))      # set the window parameters
        MainWindow.setGeometry(400, 400, 400, 170)
        MainWindow.setWindowTitle("Pace 5000 : Remote control")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8('ico\general-electrics.png')))
        MainWindow.setWindowIcon(icon)


#------- LAYOUT -------#

        self.layout_1 = QtGui.QFormLayout()                               # Create the first layout ; this part allow us to apply new parameters
        self.line_setp1 = QtGui.QLineEdit()
        self.layout_1.addRow(QtGui.QLabel("Set Point (bar):"), self.line_setp1)
        self.line_slewrate1 = QtGui.QLineEdit()
        self.layout_1.addRow(QtGui.QLabel("Aim Rate (bar/min):"), self.line_slewrate1)
        #self.rate_mode = QtGui.QComboBox()
        #self.rate_mode.addItem("")
        #self.rate_mode.addItem("MAX")
        #self.rate_mode.addItem("LIN")
        #self.layout_1.addRow(QtGui.QLabel("Rate Mode :"), self.rate_mode)
        #self.btn_apply = QtGui.QPushButton("Apply")
        #self.layout_1.addRow(self.btn_apply)

        self.layout_2 = QtGui.QFormLayout()                               # Create the second layout ; this part allow us to read the current parameters
        self.line_setp2 = QtGui.QLineEdit()
        self.layout_2.addRow(QtGui.QLabel("Set Point (bar):"), self.line_setp2)
        self.line_slewrate2 = QtGui.QLineEdit()
        self.layout_2.addRow(QtGui.QLabel("Aim Rate (bar/min):"), self.line_slewrate2)
        self.line_slewrate_act = QtGui.QLineEdit()
        self.layout_2.addRow(QtGui.QLabel("Actual Rate (bar/min):"), self.line_slewrate_act)
        self.line_pressure2 = QtGui.QLineEdit()
        self.layout_2.addRow(QtGui.QLabel("Pressure (bar) :"), self.line_pressure2)
        self.btn_read = QtGui.QPushButton("Read")
        self.layout_2.addRow(self.btn_read)

        self.layout_3 =QtGui.QGridLayout()                   # Create the third layout ; it allow us to control the device
        self.layout_3.setColumnStretch(0,1)
        self.layout_3.setColumnStretch(1,1)
        self.btn_strtm = QtGui.QPushButton("Start Control")
        self.layout_3.addWidget((self.btn_strtm),0,0)
        self.btn_stpm = QtGui.QPushButton("Measure")
        self.layout_3.addWidget((self.btn_stpm),0,1)
        alignement = QtCore.Qt.AlignCenter
        self.line_state = QtGui.QLabel("Measure Mode")
        self.line_state.setAlignment(alignement)
        self.layout_3.addWidget((self.line_state), 1, 0, 1, 0)

#------- PLOT -------#

        self.layout_p = QtGui.QGridLayout()
        self.layout_p.setGeometry(QtCore.QRect(0,0,200,200))
        self.plot_p = pg.PlotWidget(title="Pressure Control", enableMenu=True)

        self.plot_p.setLabel('left', 'Pressure', units='Bar')
        self.plot_p.setLabel('bottom', 'Time', units='s')






        self.layout_p.addWidget(self.plot_p)


#------- BOXES -------#         # Set layout's position

        HWidget = QtGui.QHBoxLayout()
        HWidget.addLayout(self.layout_1)
        HWidget.addLayout(self.layout_2)

        title_info = "Parameters"
        alignement = QtCore.Qt.AlignCenter
        group_p = QtGui.QGroupBox(title_info)
        group_p.setAlignment(alignement)
        group_p.setLayout(HWidget)

        title_meas = "Measurements"
        alignement = QtCore.Qt.AlignCenter
        group_m = QtGui.QGroupBox(title_meas)
        group_m.setAlignment(alignement)
        group_m.setLayout(self.layout_3)


        VWidget = QtGui.QVBoxLayout()
        VWidget.addWidget(group_p)
        VWidget.addWidget(group_m)


        H2Widget = QtGui.QHBoxLayout()
        H2Widget.addLayout(VWidget)
        H2Widget.addLayout(self.layout_p)


#------- CENTRAL WIDGET -------#

        self.widget = QtGui.QWidget()               # We define a central widget to display something on the screen
        self.widget.setLayout(H2Widget)
        MainWindow.setCentralWidget(self.widget)



#------- MAIN --------------#

    if __name__ == "__main__":

        app = QtGui.QApplication(sys.argv)
        MainWindow = QtGui.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())
