#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates a port or adds words. """    
    while True:
        port = int(input("Enter a port number: "))
        if port == -1:
            break
        print("Port number:", port)
        print("Words:")
        for word in word