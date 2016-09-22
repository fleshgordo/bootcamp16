import serial

"""
Easy communication with arduino
"""

# change this line according to your system
# linux /dev/ttyUSB0 or /dev/ttyACMO
# windows COM[number] for example COM3

serialInterface = '/dev/tty.usbserial'
ser = serial.Serial(serialInterface, 9600)
ser.write('5')
