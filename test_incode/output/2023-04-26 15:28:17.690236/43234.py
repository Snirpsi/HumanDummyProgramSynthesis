#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints words and stores all ports. """    
    while True:
        words = input("Enter a word: ")
        if words:
            print(words)
            ports = input("Enter a port number: ")
            if ports:
                ports = [int(port) for port in ports.split()]
                for port in ports:
                    