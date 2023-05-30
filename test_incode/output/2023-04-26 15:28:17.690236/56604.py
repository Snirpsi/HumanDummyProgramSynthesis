#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of numbers and multiplyes a port. """    
    port = int(sys.argv[1])
    
    ports = [int(i) for i in sys.argv[2:]]
    
    ports_sum = sum(ports)
    
    ports_sum = ports_sum * port
    
    print(ports_sum)
    
