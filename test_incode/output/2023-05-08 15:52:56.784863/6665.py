#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A endless loop that opens a list of numbers.
    #Each time the loop runs, it prints the next number in the list.
    #The loop ends when you enter a number that isn't in the list.
    #The program will continue to run until you enter a number that isn't in the list.
    while(True):
        number = input("Enter a number in the list: ")
        if number not in numbers:
            print("That number isn't in the list")
        else:
            print(number)
            numbers.append(number)
        else:
            break

