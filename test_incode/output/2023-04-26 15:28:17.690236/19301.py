#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates numbers. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: python enumerate_numbers.py <filename>")
        sys.exit()
    
    with open(sys.argv[1]) as file:
        for line in file:
            line = line.strip()
            
            if line == "":
                continue
            
            number = int(line)
            
            if number < 1:
                continue
            
            print(number)
            
