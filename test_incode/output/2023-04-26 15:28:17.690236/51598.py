#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens fruits. """    
    while True:
        fruit = input("What fruit do you want? ")
        if fruit == "apple":
            print("Oh, you got apple!")
        elif fruit == "orange":
            print("Oh, you got orange!")
        elif fruit == "banana":
            print("Oh, you got banana!")
        else:
            print("Oh, you got nothing!")
