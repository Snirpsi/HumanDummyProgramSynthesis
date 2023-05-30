#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints user input and prints fruits. """    
    
    fruits = ['apple', 'banana', 'cherry']
    
    while True:
        
        print('What fruit do you want?')
        
        fruit = input()
        
        if fruit in fruits:
            print('You chose ' + fruit)
        else:
            print('Sorry, that fruit does not exist!')
            
        print('Do you want to continue? Y/N')
        
        continue_