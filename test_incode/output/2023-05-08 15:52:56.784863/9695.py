#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A endless loop that stores a list of numbers.
    #The loop will terminate when the user enters a number greater than the length of the list.
    #The program will then print the list to the screen.
    while(True):
        number = int(input("Enter a number: "))
        if number > len(numbers):
            print("The list is full")
            break
        else:
            numbers.append(number)
    print(numbers)

