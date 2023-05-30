#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over fruits or returns user input. """    
    while True:
        print("Enter a fruit: ")
        fruit = input()
        print("You entered", fruit)
        
        if fruit == 'apple':
            print("You entered apple")
            break
        elif fruit == 'banana':
            print("You entered banana")
            break
        elif fruit == 'cherry':
            print("You entered cherry")
            break
        elif fruit == 'orange':
            print("You entered orange")
            break
        elif fruit == 'lemon':
            print("You entered lemon")
            break
        elif fruit == 'watermelon':
            print("You entered watermelon")
            break
        else:
            print("You entered an invalid fruit")
