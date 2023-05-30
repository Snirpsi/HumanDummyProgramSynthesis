#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds fruits. """    
    while True:
        fruit = input("Enter a fruit: ")
        fruit = fruit.upper()
        if fruit == "APPLE":
            print("You chose apple")
        elif fruit == "ORANGE":
            print("You chose orange")
        elif fruit == "PUFFIN":
            print("You chose puffin")
        elif fruit == "GRAPE":
            print("You chose grape")
        elif fruit == "GRAPE