#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that enumerates all ports. """    
    
    ports = []
    
    for port in os.listdir('/sys/class/net/'):
        ports.append(port)
        
    for port in ports:
        
        try:
            
            ifconfig = open('/sys/class/net/%s/ifconfig' % port, 'r')
            
            ifconfig.readline()
            
            ifconfig.readline()
            
            ifconfig.readline()
            
            ifconfig.readline()
            
            ifconfig.readline()
            
            ifconfig.readline()
            
            ifconfig.readline()
            
            ifconfig.readline()
            
            ifconfig.readline()
            
            ifconfig.readline()
            
            ifconfig.readline()
            
            ifconfig.readline()
            
            ifconfig.readline()
            
            ifconfig.readline()
            
            ifconfig.readline()
            
            ifconfig.readline()
            
            ifconfig.readline()
            
            ifconfig.readline()
            
            ifconfig.readline()
            
            ifconfig.readline()
            
            ifconfig.readline()
            
            ifconfig.readline()
            
            ifconfig.readline()
            
            ifconfig.readline()
            
            ifconfig.readline()
            
            ifconfig.readline()
            
            ifconfig.readline()
            
            ifconfig.readline()
            
            ifconfig.readline()
            
            ifconfig.readline()
            
            ifconfig.readline()
            
            ifconfig.readline()
            
            ifconfig.readline()
            
            ifconfig.readline()
            
            ifconfig.readline()
            
            ifconfig.readline()
            
            ifconfig.readline()
            
            ifconfig.readline()
            
            ifconfig.readline()
            
            ifconfig.readline()
            
            ifconfig.readline()
            
            ifconfig.readline()
            
            ifconfig.readline()
            
            ifconfig.readline()
            
            ifconfig.readline()
            
            ifconfig.readline()
            
            ifconfig.readline()
            
            ifconfig.readline()
            
            ifconfig.readline()
            
            ifconfig.readline()
            
            ifconfig.readline()
            
            ifconfig.readline()
            
            ifconfig.readline()
            
            ifconfig.readline()
            
            ifconfig.readline()
            
            ifconfig.readline()
            
            ifconfig.readline()
            
            ifconfig.readline()
            
            ifconfig.readline()
            
            ifconfig.readline()
            
            ifconfig.readline()
            
            ifconfig.readline()
            
            ifconfig.readline()
            
            ifconfig.readline()
            
            ifconfig.readline()
