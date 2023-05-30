#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns user input and iterates over a list of numbers. """    
    while True:
        number = int(input('Enter a number: '))
        
        # if the number is less than zero, return it
        if number < 0:
            print('The number is less than zero!')
            continue
        
        # if the number is greater than the length of the list, return it
        elif number > len(numbers):
            print('The number is greater than the length of the list!')
            continue
        
        # otherwise, add the number to the list
        else:
            numbers.append(number)
            
        # if the user enters -1, the loop will terminate
        if number == -1:
            break
        
    # print the list to the screen
    print('The numbers are:')
    print(numbers)
    
    # ask the user to input another number
    print('Enter another number: ')
    
    # get the user input
    number = int(input('Enter a number: '))
    
    # if the number is less than zero, return it
    if number < 0:
        print('The number is less than zero!')
        continue
    
    # if the number is greater than the length of the list, return it
    elif number > len(numbers):
        print('The number is greater than the length of the list!')
        continue
    
    # otherwise, add the number to the list
    else:
        numbers.append(number)
        
    # if the user enters -1, the loop will terminate
    if number == -1:
        break
    
    # print the list to the screen
    print('The numbers are:')
    print(numbers)
    
    # ask the user to input another number
    print('Enter another number: ')
    
    # get the user input
    number = int(input('Enter a number: '))
    
    # if the number is less than zero, return it
    if number < 0:
        print('The number is less than zero!')
        continue
    
    # if the number is greater than the length of the list, return it
    elif number > len(numbers):
        print('The number is greater than the length of the list!')
        continue
    
    # otherwise, add the number to the list
    else:
        numbers.append(number)
        
    # if the user enters -1, the loop will terminate
    if number == -1:
        break
    
    # print the list to the screen
    print('The numbers are:')
    print(numbers)
    
    # ask the user to input another number
    print('Enter another number: ')
    
    # get the user input
    number = int(input('Enter a number: '))
    
    # if the number is less than zero, return it
    if number < 0:
        print('The number is less than zero!')
        continue
    
    # if the number is greater than the length of the list, return it
    elif number > len(numbers):
        print('The number is greater than the length of the list!')
        continue
    
    # otherwise, add the number to the list
    else:
        numbers.append(number)