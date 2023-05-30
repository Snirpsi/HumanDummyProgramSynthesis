#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens words or returns numbers. """    
    
    import sys
    
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = input("Please enter the file name: ")
    
    try:
        f = open(filename, 'r')
        
        lines = f.readlines()
        
        f.close()
        
        numbers = []
        
        for line in lines:
            
            line = line.strip()
            
            if line == '':
                continue
            
            if line[0].isdigit():
                numbers.append(int(line))
                
            else:
                numbers.append(line)
                
        numbers = list(filter(None, numbers))
        
        print(numbers)
        
    except IOError:
        print("File not found")
        
    else:
        print("File opened")
        
        
        
