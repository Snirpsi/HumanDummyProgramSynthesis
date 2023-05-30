#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes a list of words or opens fruits. """    
    
    words = ['apple', 'banana', 'cherry']
    fruits = ['apple', 'banana', 'cherry']
    
    while True:
        
        for word in words:
            print(word*fruits)
            
        choice = input('\nWould you like to continue? Y/N: ')
        
        if choice.lower() == 'y':
            break
        else:
            print('Goodbye!')
            
    
