#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts fruits. """    
    while True:
        fruits = input("Enter a fruit (ex. apple, orange, mango): ")
        if fruits == "exit":
            break
        fruits = fruits.lower()
        if fruits == "apple":
            print("The fruit " + fruits + " is a fruit!")
        elif fruits == "orange":
            print("The fruit " + fruits + " is a fruit!")
        elif fruits == "mango":
            print("The fruit " + fruits + " is a fruit!")
        else:
            print("Sorry, I didn't understand that fruit.")
