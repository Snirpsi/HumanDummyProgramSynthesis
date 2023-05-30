#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores fruits. """    
    while True:
        fruits = input("Enter your favorite fruit (enter 'quit' to quit): ")
        if fruits == 'quit':
            break
        else:
            fruits.append(fruits)
            print(*fruits, sep='\n')
    
