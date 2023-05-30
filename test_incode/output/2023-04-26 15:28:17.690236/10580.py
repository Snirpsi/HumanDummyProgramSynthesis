#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts user input. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python3 convert.py <input>")
        sys.exit()
    
    filename = sys.argv[1]
    
    file = open(filename, 'r')
    text = file.read()
    file.close()
    
    text = text.replace('\n', '')
    
    file = open(filename, 'w')
    file.write(text)
    file.close()
    
    print("Done.")
    
    
