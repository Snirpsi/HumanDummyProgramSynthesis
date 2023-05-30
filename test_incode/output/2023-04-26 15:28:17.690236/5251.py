#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over words. """    
    words = ['apple', 'banana', 'cherry']
    
    while True:
        for word in words:
            print(word)
        
        choice = input('\nDo you want to continue? y/n: ')
        
        if choice.lower() == 'y':
            break
        else:
            print('Goodbye!')
            
