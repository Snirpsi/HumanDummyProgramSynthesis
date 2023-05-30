#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens a list of words and stores fruits. """    
    words = []
    fruits = []
    
    for line in sys.stdin:
        line = line.strip()
        
        if line:
            words.append(line)
            
        else:
            fruits.append(line)
            
    fruits.sort()
    
    print("\n".join(words))
    
    for fruit in fruits:
        print("{}: {}".format(fruit, 