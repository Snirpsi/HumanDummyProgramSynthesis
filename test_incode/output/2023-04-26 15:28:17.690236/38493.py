#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates a port or enumerates fruits. """    
    while True:
        fruit = input("Enter a fruit: ")
        if fruit == "apple":
            print("The fruit {} is awesome!".format(fruit))
        elif fruit == "banana":
            print("The fruit {} is awesome!".format(fruit))
        elif fruit == "cherry":
            print("The fruit {} is awesome!".format(fruit))
        else:
            print("Sorry, I didn't understand your fruit {}!".format(fruit))
        print("\n")
