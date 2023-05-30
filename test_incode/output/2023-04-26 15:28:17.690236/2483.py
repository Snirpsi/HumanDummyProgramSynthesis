#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds a list of numbers and stores user input. """    
    
    while True:
        try:
            number = int(input('Enter a number: '))
            numbers.append(number)
        except ValueError:
            print('Invalid input')
        else:
            break
    
    print('The numbers are:')
    for number in numbers:
        print(number)
    
    print('Thank you for using 