#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes a list of words and opens a port. """    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s <words>' % sys.argv[0])
        sys.exit()
    
    words = sys.argv[1:]
    
    for word in words:
        remove_word(word)
        
    port = '/dev/ttyUSB0'
    
    try:
        open_device(port)
    except IOError:
        print('Error: Could not open device %s' % port)
        sys.exit()
    
    print('Done.')
    
