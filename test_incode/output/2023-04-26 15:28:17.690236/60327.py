#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates fruits or converts a list of numbers. """    
    while True:
        fruit = input("Enter a fruit or a list of numbers: ")
        if fruit == 'quit':
            break
        elif fruit == '':
            continue
        else:
            fruit = int(fruit)
            if fruit < 0 or fruit > len(Fruits):
                print("Invalid input.")
                continue
            else:
                Fruits[fruit] += 1
                print("The fruit {} has {} apples.".format(Fruits[fruit], Fruits[fruit]))
                
