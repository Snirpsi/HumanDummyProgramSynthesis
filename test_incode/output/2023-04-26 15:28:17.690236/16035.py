#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes a list of words. """    
    words = ['a', 'b', 'c']
    
    while True:
        words.remove(words.pop(0))
        
        print(' '.join(words))
        
        if words == []:
            break
        
        time.sleep(1)
        
    print('Bye!')
    
    
