#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over a port or adds fruits. """    
    
    port = input("Enter a port number: ")
    
    while True:
        fruit = "apple"
        
        if port == "exit":
            break
        
        if port == "1":
            fruit = "banana"
        
        if port == "2":
            fruit = "cherry"
        
        if port == "3":
            fruit = "