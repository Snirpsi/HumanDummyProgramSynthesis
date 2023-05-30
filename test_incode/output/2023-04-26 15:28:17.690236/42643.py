#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens fruits or multiplyes user input. """    
    while True:
        fruit = input("Enter a fruit name: ")
        if fruit == "exit":
            break
        else:
            fruit = fruit.title()
            fruit = fruit.capitalize()
            fruit = fruit.lower()
            fruit = fruit.upper()
            print(fruit)
