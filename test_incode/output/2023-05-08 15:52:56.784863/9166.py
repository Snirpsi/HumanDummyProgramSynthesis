#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A program that removes a list of numbers.
    #The program should ask the user for a list of numbers to remove.
    #The program should then remove all numbers in the list.
    #The program should then print the list of numbers removed.
    #The program should then exit.
    
    #Ask the user for a list of numbers to remove.
    numbers = input("Enter a list of numbers to remove: ")
    
    #Remove all numbers in the list.
    numbers = list(filter(lambda x: x != 0, numbers))
    
    #Print the list of numbers removed.
    print(numbers)
    
    #Exit the program.
    exit()

