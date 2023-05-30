#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("usage: python remove_numbers.py <input>")
        sys.exit()
    
    with open(sys.argv[1]) as input_file:
        lines = input_file.readlines()
    
    for line in lines:
        line = line.strip()
        
        if line.isdigit():
            print(line)
        else:
            print(line)
    
