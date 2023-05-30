#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that converts a list of words or opens a list of numbers. """    
    while True:
        try:
            line = input()
            line = line.strip()
            line = line.split()
            
            number = int(line[0])
            
            if number > len(