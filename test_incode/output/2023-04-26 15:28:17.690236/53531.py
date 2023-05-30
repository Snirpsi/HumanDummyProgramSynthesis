#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that removes words or iterates over a port. """    
    while True:
        port = int(input("Enter a port number: "))
        words = []
        with open(port, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    words.append(line)
        
        words = word