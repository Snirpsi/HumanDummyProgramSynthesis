#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = input("Please enter the name of the file you want to open: ")
    
    file = open(filename, 'r')
    
    for line in file:
        line = line.strip()
        
        if line.find('#') != -1:
            continue
        
        if line.find('"') != -1:
            line = line.replace('"', '\\"')
            
        print(line)
        
    file.close()
    
