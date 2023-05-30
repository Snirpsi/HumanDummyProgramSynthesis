#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores words and iterates over a port. """    
    port = int(sys.argv[1])
    words = []
    
    while True:
        words.append(input('Enter a word: ').lower())
        
        if len(words) == port:
            print(*words, sep='\n')
            break
    
    print('\nBye!')
    
