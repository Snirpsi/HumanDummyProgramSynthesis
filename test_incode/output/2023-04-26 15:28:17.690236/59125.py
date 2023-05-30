#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <filename>" % sys.argv[0])
        sys.exit(1)
    
    filename = sys.argv[1]
    
    with open(filename, 'r') as file:
        lines = file.readlines()
        
    for line in lines:
        line = line.strip()
        
        if line.isdigit():
            line = line[1:]
            
            if line not in numbers:
                print(line)
                
            else:
                print(line)
                
        else:
            print(line)
            
