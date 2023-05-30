#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints a list of words and stores words. """    
    words = ['hello', 'world', 'python', 'is', 'fun']
    
    while True:
        print('\n'.join(words))
        
        words = input('Enter another word: ')
        
        if words:
            words.extend(words.split())
        
        else:
            break
        
    print('\nThe endless loop has ended')
    
