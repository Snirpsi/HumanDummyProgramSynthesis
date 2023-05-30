#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that opens words and returns a port. """    
    while True:
        word = input("Enter a word: ")
        port = random.randint(10000, 65535)
        print("The port is", port)
        
