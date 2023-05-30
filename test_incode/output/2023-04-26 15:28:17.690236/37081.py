#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates fruits or calculates a list of words. """    
    while True:
        fruit = input("Enter a fruit: ")
        if fruit == 'quit':
            break
        else:
            print(calculate_fruit(fruit))
