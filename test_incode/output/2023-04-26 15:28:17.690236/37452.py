#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that opens all ports. """    
    ports = open('/dev/ttyACM0','r')
    for line in ports:
        print(line)
    ports.close()
    
