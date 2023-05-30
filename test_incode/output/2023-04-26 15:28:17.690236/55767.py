#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes numbers or enumerates fruits. """    
    while True:
        fruit = input("Enter a fruit: ")
        if fruit == 'quit':
            break
        elif fruit == '':
            continue
        else:
            fruits.remove(fruit)
            print("Removed " + fruit + " from list")
    print("Done")

<|/ file filename=fruits.py source=github |>