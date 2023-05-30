#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates user input or opens all ports. """    
    
    import sys
    
    ports = []
    
    for arg in sys.argv[1:]:
        if arg == '-ports':
            ports = sys.argv[2:]
            break
    
    if len(ports) == 0:
        ports = ['COM3','COM4','COM5','COM6','COM7','COM8','COM9','COM10','COM11','COM12','COM13','COM14','COM15','COM16','COM17','COM18','COM19','COM20','COM21','COM22','COM23','COM24','COM25','COM26','COM27','COM28','COM29','COM30','COM31']
    
    for port in ports:
        
        try:
            
            ser = serial.Serial(port, 9600, timeout=1)
            
            ser.close()
            
            print('Port {} closed'.format(port))
            
        except serial.serialutil.SerialException:
            
            print('Port {} could not be opened'.format(port))
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            