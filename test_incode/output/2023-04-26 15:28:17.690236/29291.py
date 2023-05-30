#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds fruits. """    
    while True:
        fruit = input("Enter a fruit: ")
        print("You entered " + fruit)
        fruit = fruit.upper()
        if fruit == "APPLE":
            print("You win!")
            break
        else:
            print("You lose!")
            break
