#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates fruits. """    
    fruits = []
    while True:
        fruits.append(input("Enter a fruit name: ").strip())
        if fruits[-1] == '':
            break
    print("The fruits: ", fruits)
    
