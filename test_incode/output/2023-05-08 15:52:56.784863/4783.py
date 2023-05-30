#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A endless loop that removes a list of numbers.
    #The loop will run until a user enters a number that isn't in the list.
    #The loop will then exit and print a message to the user.
    while True:
        number = input("Enter a number: ")
        if number not in numbers:
            print("That number isn't in the list")
        else:
            numbers.remove(number)
            print(number)
            break

