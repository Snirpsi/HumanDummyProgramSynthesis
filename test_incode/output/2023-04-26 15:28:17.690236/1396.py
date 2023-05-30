#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates a port or removes a list of words. """    
    
    import sys
    
    if len(sys.argv) == 1:
        print('Usage: %s <port>' % sys.argv[0])
        sys.exit()
    
    port = sys.argv[1]
    
    if port == 'all':
        ports = range(1024)
    else:
        ports = [port]
    
    for port in ports:
        
        print('Enumerating port %s' % port)
        
        words = enumerateWords(port)
        
        print('\n'.join('%s -> %s' % (word, word) for word, count in words))
        
        print('\nDone.')
        
