#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens a list of numbers. """    
    numbers = [int(x) for x in input('Enter numbers: ').split()]
    while True:
        print('The numbers are:')
        for number in numbers:
            print(number)
        print('')
        print('Do you want to continue? (y/n)')
        answer = input('> ').lower()
        if answer == 'y':
            break
        elif answer == 'n':
            print('Goodbye!')
            break
        else:
            print('Sorry, I did not understand your input.')
