#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts a list of words. """    
    words = ['hello', 'world', '!']
    
    i = 0
    while True:
        
        print('Word #{}'.format(i))
        print('\t{}'.format(words[i]))
        
        i += 1
        
        if i == len(words):
            break
        
        time.sleep(1)
        
    
