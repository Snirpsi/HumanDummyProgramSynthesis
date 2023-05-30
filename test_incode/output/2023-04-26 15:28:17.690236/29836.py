#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts all ports or adds a list of words. """    
    ports = ['COM1', 'COM2', 'COM3']
    words = ['word1', 'word2', 'word3']
    
    while True:
        for port in ports:
            ser = serial.Serial(port, 9600, timeout=1)
            ser.write('AT+CMGF=1\r')
            ser.write('AT+CMGS="{}"\r'.format(words))
            ser.write('AT+CMGL="{}"\r'.format(port))
            ser.write('AT+CMGS="{}"\r'.format(words))
            ser.write('AT+CMGL="{}"\r'.format(port))
            ser.write('AT+CMGS="{}"\r'.format(words))
            ser.write('AT+CMGL="{}"\r'.format(port))
            ser.write('AT+CMGS="{}"\r'.format(words))
            ser.write('AT+CMGL="{}"\r'.format(port))
            ser.write('AT+CMGS="{}"\r'.format(words))
            ser.write('AT+CMGL="{}"\r'.format(port))
            ser.write('AT+CMGS="{}"\r'.format(words))
            ser.write('AT+CMGL="{}"\r'.format(port))
            ser.write('AT+CMGS="{}"\r'.format(words))
            ser.write('AT+CMGL="{}"\r'.format(port))
            ser.write('AT+CMGS="{}"\r'.format(words))
            ser.write('AT+CMGL="{}"\r'.format(port))
            ser.write('AT+CMGS="{}"\r'.format(words))
            ser.write('AT+CMGL="{}"\r'.format(port))
            ser.write('AT+CMGS="{}"\r'.format(words))
            ser.write('AT+CMGL="{}"\r'.format(port))
            ser.write('AT+CMGS="{}"\r'.format(words))
            ser.write('AT+CMGL="{}"\r'.format(port))
            ser.write('AT+CMGS="{}"\r'.format(words))
            ser.write('AT+CMGL="{}"\r'.format(port))
            ser.write('AT+CMGS="{}"\r'.format(words))
            ser.write('AT+CMGL="{}"\r'.format(port))
            ser.write('AT+CMGS="{}"\r'.format(words))
            ser.write('AT+CMGL="{}"\r'.format(port))
            ser.write('AT+CMGS="{}"\r'.format(words))
            ser.write('AT+CMGL="{}"\r'.format(port))
            ser.write('AT+CMGS="{}"\r'.format(words))
            ser.write('AT+CMGL="{}"\r'.format(port))
            ser.write('AT+CMGS="{}"\r'.format(words))
            ser.write('AT+CMGL="{}"