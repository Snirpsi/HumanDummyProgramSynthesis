#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates words or iterates over a port. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s <port>' % sys.argv[0])
        sys.exit(1)
    
    port = sys.argv[1]
    
    while True:
        
        word = ''
        
        if port == '':
            word = 'exit'
        else:
            word = 'word'
            
        sys.stdout.write(word + '\n')
        sys.stdout.flush()
        
        time.sleep(1)
        
        port = input('Enter a port number: ')
        
        if port == '':
            port = 'exit'
        
