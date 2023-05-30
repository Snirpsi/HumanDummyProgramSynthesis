#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = input("Enter a filename: ")
    
    words = []
    
    with open(filename) as file:
        for line in file:
            line = line.strip()
            if line != "":
                words.append(line)
    
    words.sort()
    
    for word in words:
        print(word)
        
