#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that removes words. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <file>" % sys.argv[0])
        sys.exit()
    
    filename = sys.argv[1]
    
    with open(filename) as file:
        lines = file.readlines()
    
    words = []
    for line in lines:
        line = line.strip()
        
        if line:
            words.append(line)
    
    words = [word for word in words if word not in stopwords]
    
    with open(filename, 'w') as file:
        file.write('\n'.join(words))