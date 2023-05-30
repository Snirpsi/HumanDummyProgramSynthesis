#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes fruits or opens a list of words. """    
    while True:
        fruit = input("Enter a fruit name: ")
        if fruit == 'quit':
            break
        else:
            fruit = fruit.lower()
            fruit = fruit.capitalize()
            fruits.remove(fruit)
            print("Removed 