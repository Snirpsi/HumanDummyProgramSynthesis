#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts a port. """    
    while True:
        port = int(input("Enter a port number: "))
        convert_port(port)
        time.sleep(1)
        
