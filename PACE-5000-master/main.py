
#-------IMPORTS------------------------------

import serial.tools.list_ports
import serial
import time
from PyQt4 import QtGui
import sys

import G_window                    # Import the script of our graphical interface

#-------DEF FUNCTIONS------------------------

def execution(ser, commande):
    # Code to send a command to the controller
    # send the character to the device
    ser.write(bytes(commande + '\r\n', 'UTF-8'))
    time.sleep(0.1)                                     # waiting for a response
    print(ser.outWaiting())
    print('? =', ser.inWaiting())                       # Look into the input buffer, if it's not empty it's mean that the device received our command
    out = ''
    liste = []
    reponse = []
    while (ser.inWaiting() > 0):                        # Receive and read the device's answer
        out = str(ser.read(ser.inWaiting()))
        print('Out = ', out)
        liste.append(out)
    if (len(liste) > 0):                               # If we get an answer, we take only the usefull information before retruning it
        rep = out.split(" ")[1]
        rep = rep[0:-5]
        print(' reponse = ', rep)
        return rep
    else:                                             # If there isn't any answer, we return nothing
        return()


#------- CLASSES -------#

class MainWindow(QtGui.QMainWindow, G_window.Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)

        self.btn_read.clicked.connect(self.readparam)        # We define the purpose of the buttons
        self.btn_apply.clicked.connect(self.applyparam)
        self.btn_stpm.clicked.connect(self.Stop_m)
        self.btn_strtm.clicked.connect(self.Start_m)

#-------FUNCTIONS-------
    def readparam(self):                                               # This function allow us to read the current parameters
        self.line_setp2.setText(execution(ser, ":SOUR:PRES?"))
        self.line_slewrate2.setText(execution(ser, ":SOUR:PRES:SLEW?"))
        self.line_pressure2.setTetx(execution(ser, ":SENS:PRES?"))

    def applyparam(self):                                            # This function allow us to apply new parameters
        set_p = int(self.line_setp1.text())                          # Those parameters are chosen by the user
        slew_rate = int(self.line_slewrate1.text())
        execution(ser, ":SOUR:PRES " + (set_p))
        execution(ser, ":SOUR:PRES:SLEW " + (slew_rate))

    def Stop_m(self):                                         # Turns controller off
        execution(ser, ":OUTP:STAT OFF")                      # Print the state of the device
        self.line_state.setText('OFF')
        self.line_state.setStyleSheet("QLabel {color : red}")

    def Start_m(self):                                        # Turns controller on
        choice = QtGui.QMessageBox.question(self, 'Control Mode', "Are you sure ? You could break an 8000€ device.  ",     # We put a window to warn the user
                                            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            execution(ser, ":OUTP:STAT ON")
            self.line_state.setText('Measuring ...')
            self.line_state.setStyleSheet("QLabel {color : green}")

        else:
            pass

#-------WINDOW-----------

def Main():
    app = QtGui.QApplication(sys.argv)
    form = MainWindow()
    form.show()
    app.exec_()




def discover_connect():                    # Allow us to find the COM port

    ports = list(serial.tools.list_ports.comports())         # List all the COM ports available

    for p in ports:                                          # Loop over available ports
        print("p = ", p)
        # Open the port
        ser = serial.Serial(port=p[0],                       # Set the right parameters in order to communicate with the PACE 5000
                            baudrate=9600,
                            stopbits=serial.STOPBITS_ONE,
                            bytesize=serial.EIGHTBITS,
                            xonxoff=True)

        Longueur = len(execution(ser, ':SOUR:PRES?'))      # Query something to the device
        print('Exec : longueur = ', Longueur)
        if Longueur > 0 and str(ser.isOpen()) == 'True':   # If we get an answer it's the right device
            return(ser)                                    # ser is now the right COM port
        else:
            print('Connection error. Make sure RS232 cable is connected.')
            return()




if __name__ == '__main__':                  # If we start from this file launch the folowing
    ser = discover_connect()
    Main()
    ser.close()




