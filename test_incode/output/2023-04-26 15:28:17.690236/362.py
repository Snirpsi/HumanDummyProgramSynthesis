#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores fruits or multiplyes numbers. """    
    while True:
        fruit = input("Enter a fruit (ex. apple, orange, mango): ")
        if fruit == "quit":
            break
        elif fruit == "multiply":
            number = input("Enter a number: ")
            number = int(number)
            number = number * 2
            print("The number multiplied by 2 is {}".format(number))
        elif fruit == "add":
            number = input("Enter a number: ")
            number = int(number)
            number = number + 1
            print("The number added is {}".format(number))
        else:
            print("Invalid input. Try again.")
