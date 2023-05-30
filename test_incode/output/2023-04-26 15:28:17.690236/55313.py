#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts a list of numbers or calculates all ports. """    
    
    # read the list of numbers
    numbers = []
    for line in sys.stdin:
        numbers.append(int(line))
    
    # calculate the ports
    ports = calculate_ports(numbers)
    
    # print the ports
    for port in ports:
        print(port)
        
