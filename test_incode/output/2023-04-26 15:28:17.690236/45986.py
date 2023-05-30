#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens all ports and calculates a list of numbers. """    
    ports = openports()
    numbers = []
    for port in ports:
        numbers.append(ports[port])
    print(numbers)
</code>
<|/ a dscore=0 |>
<| c |>
This code will print all numbers in all ports. OP wants to print only numbers in selected ports.
<|/ c |>
<| c |>
