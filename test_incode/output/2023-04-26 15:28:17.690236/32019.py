#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = input("Please enter the file name: ")
    
    words = []
    
    with open(filename) as file:
        for line in file:
            line = line.strip()
            
            if line == "":
                continue
            
            words.append(line)
    
    words.sort()
    
    for word in words:
        print(word)
    
