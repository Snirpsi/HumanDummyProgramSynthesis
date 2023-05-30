#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over a list of words. """    
    words = ['hello', 'world', 'how', 'are', 'you', 'doing', '?']
    
    while True:
        for word in words:
            print(word)
        
        choice = input('\nDo you want to continue? [y/n] ')
        if choice == 'y':
            break
        else:
            print('Exiting...')
            
    
