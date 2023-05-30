#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints words or calculates all ports. """    
    
    import sys
    
    if len(sys.argv) > 1:
        ports = sys.argv[1:]
    else:
        ports = ['COM1', 'COM2', 'COM3']
    
    for port in ports:
        
        try:
            
            ser = serial.Serial(port, 9600, timeout=.1)
            
            ser.write('hello')
            
            line = ser.readline()
            
            print(line)
            
            ser.close()
            
        except serial.serialutil.SerialException as e:
            
            print(e)
            
            ser.close()
            
