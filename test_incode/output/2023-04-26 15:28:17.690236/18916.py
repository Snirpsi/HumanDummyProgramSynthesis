#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes a port or enumerates words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s <port>' % sys.argv[0])
        sys.exit()
    
    port = int(sys.argv[1])
    
    words = []
    
    with open('words.txt', 'r') as words:
        for line in words:
            words.append(line.strip())
    
    with open('words.txt', 'w') as words:
        for line in words:
            word