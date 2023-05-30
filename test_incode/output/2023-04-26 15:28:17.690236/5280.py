#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes fruits and adds a list of numbers. """    
    while True:
        fruits = input("Enter a fruit: ")
        if fruits == "exit":
            break
        else:
            fruits = fruits.split()
            fruits.remove(fruits[0])
            fruits.append(int(fruits[1]))
            print(fruits)
            
