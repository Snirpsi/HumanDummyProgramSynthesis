#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python3 remove_numbers.py <filename>")
        sys.exit()
    
    filename = sys.argv[1]
    
    with open(filename, 'r') as file:
        lines = file.readlines()
        
    with open(filename, 'w') as file:
        for line in lines:
            number = int(line)
            if number > 0:
                file.write(str(number))
                file.write('\n')
                
