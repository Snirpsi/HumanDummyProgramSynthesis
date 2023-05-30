#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds fruits. """    
    while True:
        fruit = input("Enter a fruit: ")
        if fruit == 'quit':
            break
        else:
            fruit = fruit.lower()
            if fruit == 'apple':
                print(fruit)
            elif fruit == 'banana':
                print(fruit)
            elif fruit == 'cherry':
                print(fruit)
            elif fruit == '