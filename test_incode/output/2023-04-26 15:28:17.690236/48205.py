#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds numbers and opens user input. """    
    while True:
        number = int(input('Enter a number: '))
        
        if number == -1:
            break
        
        print('The number you entered is', number)
        
        print('Do you want to add another number? y/n')
        answer = input()
        
        if answer == 'y':
            number = number + int(input('Enter another number: '))
            print('The number you entered is', number)
        
        print('Do you want to quit or continue the program? y/n')
        answer = input()
        
        if answer == 'y':
            break
        
    print('Goodbye')
    
