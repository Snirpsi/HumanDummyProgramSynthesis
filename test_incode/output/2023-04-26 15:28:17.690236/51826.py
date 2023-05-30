#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds a port and converts words. """    
    
    while True:
        port = input('Enter a port number: ')
        
        if port == '':
            print('No port number entered')
        else:
            print('Converting words to numbers...')
            
            words = input('Enter a word: ').split()
            
            for word in words:
                word = word.lower()
                
                if word == '':
                    print('No word entered')
                else:
                    number = int(word)
                    
                    print('Converting %d to %d.' % (number, number+1))
                    
            print('Done.')
            
