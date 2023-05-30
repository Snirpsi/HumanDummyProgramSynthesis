#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns a list of numbers or removes a port. """    
    ports = input("Enter a port number: ")
    ports = ports.split()
    ports.remove(ports)
    print(ports)
</code>
<|/ a dscore=0 |>
<| c |>
This program works fine but when I want to run it from the terminal it says "TypeError: 