#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns user input or enumerates a list of numbers. """    
    
    while True:
        number = input("Enter a number: ")
        
        if number == 'quit':
            break
        
        if number == '1':
            print('The number is one.')
            
        elif number == '2':
            print('The number is two.')
            
        elif number == '3':
            print('The number is three.')
            
        elif number == '4':
            print('The number is four.')
            
        elif number == '5':
            print('The number is five.')
            
        elif number == '6':
            print('The number is six.')
            
        elif number == '7':
            print('The number is seven.')
            
        elif number == '8':
            print('The number is eight.')
            
        elif number == '9':
            print('The number is nine.')
            
        elif number == '0':
            print('The number is zero.')
            
        else:
            print('Invalid input.')
            
    print('Thank you for using the 