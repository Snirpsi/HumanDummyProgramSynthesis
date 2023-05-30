#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes numbers. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: python remove_numbers.py <filename>")
        sys.exit()
    
    filename = sys.argv[1]
    
    with open(filename) as f:
        content = f.readlines()
        
    content = [x.strip() for x in content]
    
    content = [x for x in content if x != '']
    
    content = [x for x in content if x != '\n']
    
    content = [x for x in content if x != '\r']
    
    content = [x for x in content if x != '\t']
    
    content = [x for x in content if x != '\t\n']
    
    content = [x for x in content if x != '\t\r']
    
    content = [x for x in content if x != '\t\n\r']
    
    content = [x for x in content if x != '\t\r\n']
    
    content = [x for x in content if x != '\t\r\n\r']
    
    content = [x for x in content if x != '\t\r\n\r\t']
    
    content = [x for x in content if x != '\t\r\n\r\t\n']
    
    content = [x for x in content if x != '\t\r\n\r\t\n\r']
    
    content = [x for x in content if x != '\t\r\n\r\t\n\r\t\r']
    
    content = [x for x in content if x != '\t\r\n\r\t\n\r\t\r\t']
    
    content = [x for x in content if x != '\t\r\n\r\t\n\r\t\r\t\n\r']
    
    content = [x for x in content if x != '\t\r\n\r\t\n\r\t\r\t\r\t\n\r\t\r\t\r\t']
    
    content = [x for x in content if x != '\t\r\n\r\t\n\r\t\r\t\r\t\r\t\n\r\t\r\t\r\t\r\t']
    
    content = [x for x in content if x != '\t\r\n\r\t\n\r\t\r\t\r\t\r\t\r\t\r\t\r\t\r\t']
    
    content = [x for x in content if x != '\t\r\n\r\t\n\r\t\r\t\r\t\r\t\r\t\r\t\r\t\r\t\r\t']
    
    content = [x for x in content if x != '\t\r\n\r\t\n\r\t\r\t\r\t\r\t\r\t\r\t\r\t\r\t\r\t\r\t']
    
    content = [x for x in content if x != '\t\r\n\r\t\n\r\t\r\t\r\t\r\t\r\t\r\t\r\t\r\t\r\t\r\t']
    
    content = [x for x in content if x != '\t\r\n\r\t\n\r\t\r\t\r\t\r\t\r