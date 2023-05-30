#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a port and converts words. """    
    port = int(sys.argv[1])
    
    words = []
    
    while True:
        line = input('Enter a word: ')
        
        if line == '':
            break
        
        words.append(line)
        
    print('\n'.join(words))
    
    print('\nPress Ctrl+C to quit.')
    
