#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes a port and stores a list of words. """    
    port = int(sys.argv[1])
    words = []
    while port > 0:
        words.append(str(port*2))
        port -= 1
    print('\n'.join(words))
