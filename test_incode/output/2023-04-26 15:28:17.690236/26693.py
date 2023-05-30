#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens fruits. """    
    
    while True:
        fruit = input("Enter a fruit: ")
        if fruit == "apple":
            print("Oh no! You chose apple!")
        elif fruit == "orange":
            print("Oh no! You chose orange!")
        elif fruit == "banana":
            print("Oh no! You chose banana!")
        else:
            print("Sorry, I didn't understand that!")
            
