#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over words or calculates a port. """    
    while True:
        word = input("Enter a word: ")
        port = int(input("Enter a port number: "))
        if word == "quit":
            break
        else:
            print(word, port)
            
