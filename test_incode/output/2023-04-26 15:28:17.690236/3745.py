#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts numbers or adds a list of words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python3 {} <filename>".format(sys.argv[0]))
        exit(1)
    
    filename = sys.argv[1]
    
    file = open(filename, 'r')
    
    words = []
    
    for line in file:
        line = line.strip()
        
        if line == '':
            continue
        
        if line[0].isdigit():
            words.append(line)
            
        else:
            words += line.split()
            
    file.close()
    
    words = list(set(words))
    
    words.sort()
    
    file = open(filename, 'w')
    
    for word in words:
        file.write(word + '\n')
    
    file.close()
    
    print("Done.")
    
