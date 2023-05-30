#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over all ports or calculates a list of numbers. """    
    ports = [int(port) for port in sys.argv[1:]]
    numbers = calculate_numbers(ports)
    print(numbers)
    
