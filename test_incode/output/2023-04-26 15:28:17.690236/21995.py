#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts words or prints fruits. """    
    
    import sys
    
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = input("Enter a filename: ")
    
    file = open(filename, 'r')
    
    for line in file:
        line = line.strip()
        
        if line == '':
            continue
        
        if line[0].isalpha():
            print(line)
        else:
            words = line.split()
            
            for word in words:
                print(word)
    
    file.close()
    
