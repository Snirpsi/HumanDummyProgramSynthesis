#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A program that opens a list of numbers.
    #It then prints the numbers in the list one by one.
    #It then asks the user if they want to continue or quit.
    #If the user enters yes, it prints the next number in the list.
    #If the user enters no, it quits.
    continue_or_quit = input('Do you want to continue? ')
    if continue_or_quit == 'yes':
        print('Printing numbers...')
        for number in numbers:
            print(number)
        print('Quitting...')
    else:
        print('Quitting...')

