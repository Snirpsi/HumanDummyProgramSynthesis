#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds numbers and returns all ports. """    
    
    ports = []
    
    while True:
        ports.append(random.randint(1024, 65535))
        
        print(ports)
        
        time.sleep(1)
    
