#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts a list of numbers and removes a list of numbers. """    
    
    import sys
    
    if len(sys.argv) != 3:
        print("Usage: python remove_numbers.py <input_file> <output_file>")
        sys.exit()
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    with open(input_file) as input_file:
        lines = input_file.readlines()
    
    with open(output_file, 'w') as output_file:
        for line in lines:
            number = int(line)
            if number in 