#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes numbers. """    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: python remove_numbers.py <filename>')
        sys.exit()
    
    filename = sys.argv[1]
    
    with open(filename, 'r') as f:
        lines = f.readlines()
        
    for line in lines:
        line = line.strip()
        
        if line:
            line = line.strip('\n')
            
            if line[0] == '#':
                continue
            
            if line[0] == '-':
                continue
            
            if line[0].isdigit():
                line = line[1:]
                
                print(line)
                
            else:
                print('Invalid line: ' + line)
                
    