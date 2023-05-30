#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes numbers. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python3 remove_numbers.py <file>")
        sys.exit()
    
    file = open(sys.argv[1], 'r')
    
    for line in file:
        line = line.strip()
        
        if line:
            line = line.split()
            
            if len(line) > 1:
                line = line[1:]
                
                number = int(line[0])
                
                if number > 9:
                    number = number - 9
                    
                line = line[0] + ' ' + str(number)
                
                file.write(line)
                
    file.close()
    
    print("Done.")

<|/ file ext=.py source=github |>