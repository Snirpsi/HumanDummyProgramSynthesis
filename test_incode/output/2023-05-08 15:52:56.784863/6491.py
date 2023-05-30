#!/usr/bin/python3
numbers = [1,2,3]
if __name__ == '__main__':
    #A program that stores numbers.
    #The program will ask the user to enter a number.
    #The program will then store that number in a list.
    #The program will then print the list.
    numbers = []
    while True:
        number = int(input('Enter a number: '))
        if number in numbers:
            print('That number already exists.')
        else:
            numbers.append(number)
            print('The number you entered is', number)
            break
    print('The numbers you entered were', numbers)

