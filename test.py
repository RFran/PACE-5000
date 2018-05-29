import serial.tools.list_ports
import serial
import time



    #ser = serial.Serial(port='COM12',
    #                    baudrate=9600)

def execution(ser, commande):

    # Code to send a command to the controller
    # send the character to the device
    ser.write(bytes(commande + '\r\n', 'UTF-8'))
    time.sleep(0.1)
    print(ser.outWaiting())
    print('? =',ser.inWaiting())
    out = ''

    liste = []
    reponse = []
    while (ser.inWaiting() > 0):
        out = str(ser.read(ser.inWaiting()))
        print('Out = ', out)
        liste.append(out)

    if (len(liste) > 0):

        rep = out.split(" ")[1]
        rep = rep[0:-5]

        print(' reponse = ', rep)
        return rep
    else:
        return()



    ser.flushInput()
    ser.flushOutput()



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


        #execution(ser, ':OUTP 1')    # Commande interdite !!!!!!!


        Longueur = len(execution(ser, ':SOUR:PRES?'))
        print('Exec : longueur = ', Longueur)
        if Longueur > 0 and str(ser.isOpen()) == 'True':
            return(ser)
        else:
            print('Connection error. Make sure RS232 cable is connected.')
            return()




ser = discover_connect()
print("Connécté au port :", ser)

execution(ser, ':SOUR:PRES 10')
execution(ser, ':SOUR:PRES?')


ser.close()

