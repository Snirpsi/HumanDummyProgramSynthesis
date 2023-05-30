#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores a list of numbers and removes a port. """    
    ports = [8080, 8081, 8082, 8083, 8084, 8085]
    while True:
        ports.remove(8080)
        print("Port %d is gone" % port)
        
