#!/usr/bin/python3
if __name__ == '__main__':
    #A program that converts user input.
    #It will ask the user for an integer, and convert it to a string.
    #The program will then print out the string and an integer in reverse order.
    
    number = int(input('Enter a number: '))
    
    string = str(number)
    
    string = string[::-1]
    
    print(string)
    print(number)

