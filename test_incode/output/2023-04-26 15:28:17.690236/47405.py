#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores words or calculates a list of numbers. """    
    
    import sys
    
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = input("Enter the file name: ")
    
    words = []
    
    with open(filename) as f:
        for line in f:
            line = line.strip()
            
            if line != "":
                words.append(line)
    
    numbers = []
    
    with open(filename) as f:
        for line in f:
            line = line.strip()
            
            if line != "":
                numbers.append(line)
    
    words.sort()
    numbers.sort()
    
    print("\n".join(words))
    print("\n".join(numbers))
    
    
