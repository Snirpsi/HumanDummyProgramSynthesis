#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes numbers. """    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: python3 remove_numbers.py <filename>")
        sys.exit()
    
    with open(sys.argv[1], 'r') as file:
        lines = file.readlines()
        
        for line in lines:
            line = line.strip()
            
            if line.isdigit():
                line = line.replace(line, "")
            
            print(line)
            
    file.close()
    
