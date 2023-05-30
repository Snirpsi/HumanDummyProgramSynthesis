#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that prints user input and opens words. """    
    while True:
        line = input()
        line = line.strip()
        if line == 'exit':
            break
        else:
            print(line)
