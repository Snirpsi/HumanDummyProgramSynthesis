#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns a port. """    
    while True:
        port = random.randint(10000, 65535)
        print("Server running on port " + str(port))
        
