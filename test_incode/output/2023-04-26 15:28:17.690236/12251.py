#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes words and returns a port. """    
    while True:
        word = ""
        port = ""
        while word != "stop":
            word = input("Enter a word: ")
            port += word
        print("The port is: " + port)
