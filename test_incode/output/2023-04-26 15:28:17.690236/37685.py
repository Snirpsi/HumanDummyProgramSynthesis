#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that iterates over user input. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("usage: python iterate_over_input.py <input_file>")
        exit(1)
        
    input_file = sys.argv[1]
    
    with open(input_file) as input_file:
        for line in input_file:
            print(line)
            
