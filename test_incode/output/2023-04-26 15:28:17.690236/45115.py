#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes numbers. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print('Usage: python3 remove_numbers.py <filename>')
        sys.exit()
    
    with open(sys.argv[1], 'r') as file:
        lines = file.readlines()
    
    for line in lines:
        line = line.strip()
        
        if line:
            line = line.strip('\n')
            
            if line[0].isdigit():
                line = line[1:]
                
                print(line)
    
    print('Done.')
    
