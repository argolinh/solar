
# pyserial para comunicacao das portas

import serial 
# configuracao da porta serial 
ser = serial.Serial('COM3', 9600)

while True:
    line = ser.readline().decore('utf-8').rstrip()
    print(line)


