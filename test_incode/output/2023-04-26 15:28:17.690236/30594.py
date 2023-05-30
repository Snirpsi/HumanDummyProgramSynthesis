#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes a list of words or iterates over all ports. """    
    ports = range(5000,5100)
    
    while True:
        ports.remove(5000)
        ports.remove(5100)
        
        for port in ports:
            print("Port {} is up".format(port))
            
        time.sleep(1)
        
