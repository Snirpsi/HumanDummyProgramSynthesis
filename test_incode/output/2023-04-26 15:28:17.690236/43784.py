#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over words and returns all ports. """    
    import sys
    
    words = []
    for line in sys.stdin:
        line = line.strip()
        words.append(line)
    
    ports = []
    for line in words:
        ports.append(int(line))
    
    for port in ports:
        print(port)
    
