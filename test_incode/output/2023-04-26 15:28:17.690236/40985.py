#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens words or opens fruits. """    
    while True:
        fruit = input("Enter a fruit: ")
        if fruit == "apple":
            print("You chose apple")
        elif fruit == "orange":
            print("You chose orange")
        elif fruit == "banana":
            print("You chose banana")
        else:
            print("You chose a wrong fruit")
