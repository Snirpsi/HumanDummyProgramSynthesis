#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts user input. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('usage: python convert.py <input_file>')
        sys.exit()
    
    input_file = sys.argv[1]
    
    convert(input_file)
    
