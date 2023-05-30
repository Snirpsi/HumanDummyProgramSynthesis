#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes a port or adds fruits. """    
    while True:
        port = input("Enter a port number: ")
        if port == "quit":
            break
        elif port == "add":
            fruits = ["apple", "banana", "cherry"]
            fruits.remove(port)
            print("The fruit " + port + " has been removed.")
        elif port == "remove":
            fruits = ["apple", "banana", "cherry"]
            fruits.append(port)
            print("The fruit " + port + " has been added.")
        else:
            print("Invalid input.")
