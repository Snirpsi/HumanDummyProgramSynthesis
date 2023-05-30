#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over a port. """    
    port = '/dev/ttyUSB0'
    
    ports = [port]
    
    while True:
        for port in ports:
            
            try:
                s = serial.Serial(port, 9600)
                s.close()
                
                print('Port %s closed' % port)
                
            except serial.serialutil.SerialException:
                print('Port %s closed' % port)
                
        ports.remove(port)
        
        time.sleep(1)
        
