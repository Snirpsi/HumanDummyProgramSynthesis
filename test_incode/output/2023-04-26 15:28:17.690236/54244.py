#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates all ports or adds a list of words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        ports = sys.argv[1:]
    else:
        ports = ['COM1', 'COM2', 'COM3']
    
    for port in ports:
        try:
            ser = serial.Serial(port, 9600, timeout=3)
            ser.write('hello\n')
            ser.write('world\n')
            ser.write('goodbye\n')
            ser.close()
        except serial.serialutil.SerialException:
            print('Port %s is not open' % port)
            
    print('Done')
    
