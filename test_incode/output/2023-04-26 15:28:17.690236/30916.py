#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that calculates a port and removes a list of words. """    
    while True:
        port = int(input("Enter a port number: "))
        words = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        removed = [word for word in words if word not in words]
        removed = " ".join(removed)
        print("The port number you entered is", port, "and the words you removed are", removed)
