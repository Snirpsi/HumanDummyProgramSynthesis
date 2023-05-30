#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over fruits and opens fruits. """    
    
    fruits = open('fruits.txt')
    
    for line in fruits:
        line = line.strip()
        
        if line == '':
            continue
        
        print(line)
    
    fruits.close()
    
