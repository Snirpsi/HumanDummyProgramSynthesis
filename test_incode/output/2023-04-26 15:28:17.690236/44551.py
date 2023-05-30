#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes words or calculates a port. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: python %s <word>' % sys.argv[0])
        exit(1)
    
    word = sys.argv[1]
    
    port = int(word) * int(word)
    
    print('Port: %d' % port)
    
