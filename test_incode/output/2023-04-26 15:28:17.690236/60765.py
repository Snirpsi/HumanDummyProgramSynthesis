#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates a port and returns a list of numbers. """    
    
    ports = []
    
    while True:
        ports.append(random.randint(1,65535))
        
        if ports[-1] == 65535:
            ports.pop()
            
        print('Port {} is open'.format(ports[-1]))
        
        time.sleep(1)
        
