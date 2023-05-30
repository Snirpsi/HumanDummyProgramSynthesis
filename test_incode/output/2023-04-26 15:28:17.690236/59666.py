#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates words and prints all ports. """    
    import sys
    words=[]
    for line in sys.stdin:
        line = line.strip()
        if line:
            words.append(line)
    ports=[]
    for line in sys.stdin:
        line = line.strip()
        if line:
            ports.append(line)
    words.sort()
    ports.sort()
    for word in words:
        print(word)
    for port in ports:
        print(port)
