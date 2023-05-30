#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes fruits or converts user input. """    
    while True:
        fruit = input("Enter a fruit: ")
        if fruit == "apple":
            print("The fruit is", fruit, "and it's an apple!")
        elif fruit == "orange":
            print("The fruit is", fruit, "and it's an orange!")
        elif fruit == "banana":
            print("The fruit is", fruit, "and it's a banana!")
        else:
            print("Sorry, I didn't understand that.")
