#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints all ports or multiplyes fruits. """    
    ports = [int(i) for i in sys.argv[1].split('/')]
    fruits = [0] * len(ports)
    
    for i in range(len(ports)):
        fruits[i] = ports[i] * int(sys.argv[2])
        
    print('\n'.join(map(str, fruits)))
    
