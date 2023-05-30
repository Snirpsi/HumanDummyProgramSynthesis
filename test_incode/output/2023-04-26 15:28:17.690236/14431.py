#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts a port and adds a list of numbers. """    
    port = int(sys.argv[1])
    numbers = sys.argv[2:]
    
    ports = [port]
    for number in numbers:
        ports.append(int(number))
        
    ports.sort()
    
    for port in ports:
        print('Port {} has {} numbers'.format(port, len(ports)))
    
