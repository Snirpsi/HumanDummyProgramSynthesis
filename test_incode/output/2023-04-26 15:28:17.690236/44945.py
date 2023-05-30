#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts a list of words or converts a port. """    
    
    import sys
    
    if len(sys.argv) > 1:
        words = sys.argv[1:]
    else:
        words = sys.argv[0]
    
    words = words.split()
    
    ports = []
    
    for word in words:
        ports.append(int(word))
    
    ports.sort()
    
    for port in ports:
        print('Port #{}: {}'.format(port, words[port]))
    
