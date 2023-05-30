#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints all ports or calculates words. """    
    
    ports = [
        str(port) for port in range(1, 65535)
    ]
    
    while True:
        words = ports
        
        ports = [
            port + word for word in ports
        ]
        
        print('\n'.join(words))
        
        time.sleep(1)
        
