#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes fruits or calculates fruits. """    
    while True:
        fruit = input("Enter a fruit: ")
        if fruit == 'quit':
            break
        else:
            fruits = fruit * 2
            print("The fruit is", fruits)
            
