#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes numbers. """    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: python3 remove-numbers.py <input-file>')
        exit(1)
    
    with open(sys.argv[1], 'r') as input_file:
        for line in input_file:
            if line[0] != '#':
                line = line.strip()
                line = line.split()
                
                if len(line) < 2:
                    continue
                
                if line[1] == '-':
                    line = line[2:]
                else:
                    line = line[1:]
                
                