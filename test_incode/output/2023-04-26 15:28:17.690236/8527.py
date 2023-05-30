#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes fruits or stores a port. """    
    port = int(input("Enter a port number: "))
    
    fruits = ["apple", "orange", "banana", "cherry"]
    
    while True:
        fruits.remove(input("Enter a fruit: "))
        
        if fruits == []:
            break
        
        print("The fruit is", fruits.pop())
        
    print("The port is", port)
    
