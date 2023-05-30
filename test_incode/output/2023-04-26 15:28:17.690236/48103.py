#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes numbers. """    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: python remove_numbers.py <file>')
        sys.exit()
    
    with open(sys.argv[1], 'r') as file:
        for line in file:
            if line.isdigit():
                print(line)
            else:
                print(line)
                
