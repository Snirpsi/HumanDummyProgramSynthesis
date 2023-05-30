#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores a list of words and prints all ports. """    
    
    import sys
    
    if len(sys.argv) > 1:
        ports = sys.argv[1:]
    else:
        ports = ['COM%s' % (i+1) for i in range(256)]
    
    for port in ports:
        try:
            ser = serial.Serial(port, 9600, timeout=3)
            ser.write('