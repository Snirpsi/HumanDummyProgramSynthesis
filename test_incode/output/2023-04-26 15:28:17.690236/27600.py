#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that prints fruits or prints user input. """    
    fruit = input("Enter a fruit (apple, orange, mango): ")
    if fruit == "apple":
        print("Apple")
    elif fruit == "orange":
        print("Orange")
    elif fruit == "mango":
        print("Mango")
    else:
        print("Invalid input")
