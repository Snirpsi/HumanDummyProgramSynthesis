#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens a list of numbers or multiplyes all ports. """    
    
    ports = sys.argv[1:]
    
    if len(ports) == 1:
        ports = [int(ports[0])]
    
    for port in ports:
        port = int(port)
        
        if port > 0:
            
            print('Opening port {}...'.format(port))
            
            openPort = os.popen('sudo netstat -anp | grep {}'.format(port))
            
            openPort.read()
            
            openPort.close()
            
            print('Opened port {}!'.format(port))
            
        else:
            print('Multiplying ports {}...'.format(port))
            
            multiplyPorts = os.popen('sudo netstat -anp | grep {}'.format(port))
            
            multiplyPort.read()
            
            multiplyPort.close()
            
            print('Multiplyed ports {}!'.format(port))
            
