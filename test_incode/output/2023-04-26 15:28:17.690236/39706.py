#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds user input or calculates fruits. """    
    while True:
        fruits = input("Enter a fruit (apple, orange, mango): ")
        fruit = fruits.lower()
        if fruit == 'apple':
            print("The fruit is", fruits, "and it's an apple!")
        elif fruit == 'orange':
            print("The fruit is", fruits, "and it's an orange!")
        elif fruit == 'mango':
            print("The fruit is", fruits, "and it's an mango!")
        else:
            print("Sorry, I didn't understand that fruit.")
            break
    
