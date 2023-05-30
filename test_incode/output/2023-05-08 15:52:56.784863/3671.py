#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A program that opens a list of numbers.
    #It then prints the numbers one by one to the screen.
    #It then asks the user if they want to quit or continue to next number.
    #If the user enters quit then it will quit the program.
    #If the user enters continue then it will continue to next number.
    #If the user enters anything else then it will print an error message.
    while True:
        number = int(input('Enter a number: '))
        if number in numbers:
            print(number)
        else:
            print('That number is not in the list')
        if input('Do you want to quit or continue to the next number? ').lower() == 'quit':
            break
        else:
            print('That is not an option')

