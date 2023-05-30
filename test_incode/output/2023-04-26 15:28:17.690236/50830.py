#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns a port or opens a list of words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        port = sys.argv[1]
    else:
        port = '8080'
    
    words = []
    
    with open('words.txt', 'r') as words:
        for line in words:
            words.append(line.strip())
    
    with open('ports.txt', 'w') as ports:
        ports.write(port)
    
    with open('words.txt', 'w') as words:
        for line in words:
            ports.write(line)
    
    print('Port: ' + str(port))
    print('Words: ' + str(words))
    
