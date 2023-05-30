#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates words. """    
    words = ['word1', 'word2']
    
    while True:
        for word in words:
            print(word)
        
        choice = input('\nEnter a choice: ')
        
        if choice == 'q':
            break
        
        if choice == '