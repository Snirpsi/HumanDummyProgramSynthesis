#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores words or multiplyes a port. """    
    while True:
        word = input("Enter a word: ")
        port = input("Enter a port: ")
        port = int(port)
        if port > 0 and port < 65535:
            port = str(port)
            print(word * port)
        else:
            print("Invalid port")
        
