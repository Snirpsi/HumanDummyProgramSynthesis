#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints words or converts all ports. """    
    import sys
    if len(sys.argv) > 1:
        ports = sys.argv[1:]
    else:
        ports = ['COM1', 'COM2', 'COM3']
    
    for port in ports:
        try:
            ser = serial.Serial(port, 9600, timeout=1)
            ser.write('hello\n')
            ser.write('world\n')
            ser.write('bye\n')
            ser.write('bye\n')
            ser.write('bye\n')
            ser.write('bye\n')
            ser.write('bye\n')
            ser.write('bye\n')
            ser.write('bye\n')
            ser.write('bye\n')
            ser.write('bye\n')
            ser.write('bye\n')
            ser.write('bye\n')
            ser.write('bye\n')
            ser.write('bye\n')
            ser.write('bye\n')
            ser.write('bye\n')
            ser.write('bye\n')
            ser.write('bye\n')
            ser.write('bye\n')
            ser.write('bye\n')
            ser.write('bye\n')
            ser.write('bye\n')
            ser.write('bye\n')
            ser.write('bye\n')
            ser.write('bye\n')
            ser.write('bye\n')
            ser.write('bye\n')
            ser.write('bye\n')
            ser.write('bye\n')
            ser.write('bye\n')
            ser.write('bye\n')
            ser.write('bye\n')
            ser.write('bye\n')
            ser.write('bye\n')
            ser.write('bye\n')
            ser.write('bye\n')
            ser.write('bye\n')
            ser.write('bye\n')
            ser.write('bye\n')
            ser.write('bye\n')
            ser.write('bye\n')
            ser.write('bye\n')
            ser.write('bye\n')
            ser.write('bye\n')
            ser.write('bye\n')
            ser.write('bye\n')
            ser.write('bye\n')
            ser.write('bye\n')
            ser.write('bye\n')
            ser.write('bye\n')
            ser.write('bye\n')
            ser.write('bye\n')
            ser.write('bye\n')
            ser.write('bye\n')
            ser.write('bye\n')
            ser.write('bye\n')
            ser.write('bye\n')
            ser.write('bye\n')
            ser.write('bye\n')
            ser.write('bye\n')
            ser.write('bye\n')
            ser.write('bye\n')
            ser.write('bye\n')
            ser.write('bye\n')
            ser.write('bye\n')
            ser.