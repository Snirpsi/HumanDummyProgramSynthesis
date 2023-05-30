#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a list of words and adds all ports. """    
    import sys
    
    words = []
    for line in sys.stdin:
        words.append(line.strip())
    
    ports = []
    for line in sys.stdin:
        ports.append(int(line.strip()))
    
    words.sort()
    ports.sort()
    
    words_and_ports = []
    for word in words:
        for port in ports:
            words_and_ports.append((word, port))
    
    for word, port in words_and_ports:
        print('{}: {}'.format(word, port))
    
