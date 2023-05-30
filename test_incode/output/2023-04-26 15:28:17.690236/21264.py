#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts words and enumerates fruits. """    
    
    import sys
    
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = input("Enter the filename to convert: ")
    
    file = open(filename, 'r')
    
    for line in file:
        line = line.strip()
        
        if line == '':
            continue
        
        words = line.split()
        
        for word in words:
            print(word, end=' ')
            
        print('')
    
    file.close()
    
