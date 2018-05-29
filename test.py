import serial.tools.list_ports
import serial
import time



    #ser = serial.Serial(port='COM12',
    #                    baudrate=9600)

def execution(ser, commande):

    # Code to send a command to the controller
    # send the character to the device
    ser.write(bytes(commande + '\r\n', 'UTF-8'))
    print(ser.inWaiting())
    out = ''

    liste = []
    reponse = []
    #while ser.inWaiting() > 0:
    out = str(ser.read(1))
    liste.append(out)
    print('liste = ', liste)
    if (len(liste) > 0):

        #del liste[len(liste) - 1]
        for car in liste:
            reponse.append(car[1])  # Answer is in a list of caracters --> a simple word (rep)
    rep = str()
    for i in range(len(reponse)):
        rep += reponse[i]
    print(' rep = ', rep)

    ser.flushInput()
    ser.flushOutput()

    return rep

def discover_connect():

    ports = list(serial.tools.list_ports.comports())

    for p in ports:
        print("p = ", p)
        # Open the port
        ser = serial.Serial(port=p[0],
                            baudrate=9600,
                            stopbits=serial.STOPBITS_ONE,
                            bytesize=serial.EIGHTBITS,
                            xonxoff=True)
        execution(ser, ':SOURT 10')
        longueur = len(execution(ser, ':SYST:ERR?'))
        print('Exec : longueur = ', longueur)
        if longueur > 0 and str(ser.isOpen()) == 'True':
            break

    return (ser)


ser = discover_connect()
ser.close()

