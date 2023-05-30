#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts a list of numbers or multiplyes fruits. """    
    while True:
        fruits = input('Enter a fruit: ')
        if fruits == 'exit':
            break
        else:
            fruits = int(fruits)
            if fruits > 0:
                print(fruits * 'apple')
            else:
                print(fruits * 'banana')
