#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates a port and prints a list of words. """    
    
    port = '/dev/ttyUSB0'
    
    words = []
    
    while True:
        
        words = words + [' '.join([str(ord(c)) for c in word])
                         for word in open(port, 'rb').read().splitlines()]
        
        sys.stdout.write(''.join(words))
        
        sys.stdout.flush()
        
        time.sleep(1)
        
