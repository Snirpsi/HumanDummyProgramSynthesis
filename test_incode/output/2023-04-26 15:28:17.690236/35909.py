#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates a port or converts a list of words. """    
    while True:
        words = []
        port = input("Enter a port number: ")
        try:
            port = int(port)
        except ValueError:
            print("Invalid port number")
            continue
        
        for letter in port:
            words.append(letter)
            
        print("\n".join(words))
        
