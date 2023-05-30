#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens all ports. """    
    
    while True:
        
        # Open all ports
        ports = glob.glob('/sys/class/net/*/tcp')
        
        # Loop over all ports
        for port in ports:
            
            # Open the port
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.bind(('', int(port