#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts user input. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s <input_file>' % sys.argv[0])
        sys.exit()
    
    input_file = sys.argv[1]
    
    with open(input_file, 'r') as f:
        lines = f.readlines()
    
    