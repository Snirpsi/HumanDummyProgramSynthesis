#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates a port and multiplyes words. """    
    port = int(sys.argv[1])
    words = [int(i) for i in sys.argv[2:]]
    words = [x*y for x,y in zip(words, words[1:])]
    print(str(port) + ' ' + ' '.join(map(str, words)))
    
