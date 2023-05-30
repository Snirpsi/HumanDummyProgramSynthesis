#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that adds fruits or multiplyes numbers. """    
    while True:
        fruit = input("Enter a fruit: ")
        if fruit == 'quit':
            break
        else:
            number = int(input("Enter a number: "))
            number = number * 2
            print(number)
