#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that stores a port and converts a list of words. """    
    port = int(sys.argv[1])
    words = sys.argv[2:]
    
    ports = [port]
    
    for word in words:
        ports.append(int(word))
    
    ports.sort()
    
    print(ports)
    
