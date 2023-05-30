#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes fruits or multiplyes numbers. """    
    while True:
        fruit = input("Enter a fruit or number: ")
        if fruit == "fruit":
            fruit = input("Enter a fruit or number: ")
            fruit = int(fruit)
            fruit = fruit*2
            print(fruit)
        elif fruit == "number":
            number = input("Enter a number: ")
            number = int(number)
            number = number*2
            print(number)
        else:
            print("Invalid input")
