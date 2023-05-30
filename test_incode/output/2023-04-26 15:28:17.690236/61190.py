#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates fruits or removes a list of words. """    
    
    fruits = ['apple', 'banana', 'cherry']
    
    while True:
        word = input('Enter a word: ')
        
        if word in fruits:
            print('The word "' + word + '" is in the fruits list')
        else:
            print('The word "' + word + '" is not in the fruits list')
            
        print('Would you like to enter another word? (y/n)')
        
        ans = input('(y/n)')
        
        if ans == 'y':
            continue
        elif ans == 'n':
            break
        else:
            print('Invalid input')
            
    print('Goodbye!')
    
