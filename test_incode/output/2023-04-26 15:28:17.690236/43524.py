#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints fruits. """    
    while True:
        fruit = input("Enter a fruit: ")
        if fruit == "apple":
            print("Apple!")
        elif fruit == "banana":
            print("Banana!")
        elif fruit == "cherry":
            print("Cherry!")
        else:
            print("No fruit found!")
