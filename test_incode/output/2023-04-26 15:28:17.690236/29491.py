#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = input("Enter the filename: ")
    
    with open(filename) as f:
        content = f.read()
    
    content = content.replace("\n", "")
    
    words = content.split()
    
    words = [word.lower() for word in words]
    
    words = [word for word in words if word.isalpha()]
    
    words = [word for word in words if word not in "