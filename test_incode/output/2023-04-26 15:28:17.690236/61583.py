#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s number" % sys.argv[0])
        sys.exit()
    
    number = sys.argv[1]
    
    file = open(number, 'r')
    
    for line in file:
        line = line.strip()
        
        if len(line) == 0:
            continue
        
        number = int(line)
        
        if number % 2 == 0:
            print(number)
        else:
            print(number + 1)
            
    file.close()
    
