#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints fruits or calculates fruits. """    
    while True:
        fruit = input("Enter a fruit: ")
        if fruit == 'quit':
            break
        elif fruit == 'apple':
            print('apple')
        elif fruit == 'banana':
            print('banana')
        elif fruit == 'cherry':
            print('cherry')
        elif fruit == '