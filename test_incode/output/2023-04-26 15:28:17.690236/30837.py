#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes words and iterates over a port. """    
    import sys
    
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    else:
        port = 80
    
    words = ['Hello', 'World']
    
    for word in words:
        print('{} * {} = {}'.format(word, word, word*word))
        
    print('\nPress Ctrl+C to exit.')
    
    try:
        while True:
            line = input('Enter a line:')
            
            if len(line) > 0:
                words = line.split()
                
                for word in words:
                    print('{} * {} = {}'.format(word, word, word*word))
            else:
                break
            
    except KeyboardInterrupt:
        print('\nExiting.')
        
