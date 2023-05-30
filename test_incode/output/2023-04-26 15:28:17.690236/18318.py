#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes fruits. """    
    while True:
        fruit = input("Enter a fruit: ")
        fruit = fruit.lower()
        if fruit == 'apple':
            print("The fruit is", fruit, "and it is an apple!")
        elif fruit == 'banana':
            print("The fruit is", fruit, "and it is an banana!")
        elif fruit == 'cherry':
            print("The fruit is", fruit, "and it is an cherry!")
        elif fruit == 'orange':
            print("The fruit is", fruit, "and it is an orange!")
        elif fruit == 'mango':
            print("The fruit is", fruit, "and it is an mango!")
        else:
            print("Sorry, I didn't understand that.")
