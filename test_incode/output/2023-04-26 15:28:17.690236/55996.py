#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts words or converts all ports. """    
    import sys
    if len(sys.argv) > 1:
        ports = sys.argv[1:]
    else:
        ports = ['COM%s' % (i+1) for i in range(256)]
    
    for port in ports:
        try:
            ser = serial.Serial(port, 9600, timeout=1)
            ser.write('')
        except serial.serialutil.SerialException:
            print("Port %s is not open" % port)
            sys.exit(1)
        else:
            print("Port %s is open" % port)
            sys.exit(0)

<|/ file source=github ext=.py |>