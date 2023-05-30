#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes all ports and calculates words. """    
    ports = [int(i) for i in sys.argv[1].split(',')]
    words = []
    for port in ports:
        words.append(str(port*