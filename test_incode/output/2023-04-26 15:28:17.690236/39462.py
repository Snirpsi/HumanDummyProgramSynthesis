#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over user input and adds fruits. """    
    while True:
        fruit = input("Enter a fruit: ")
        if fruit == "quit":
            break
        else:
            print("Fruit added: " + fruit)
            
    
