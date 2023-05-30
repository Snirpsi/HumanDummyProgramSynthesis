#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes words. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <filename>" % sys.argv[0])
        sys.exit(1)
    
    filename = sys.argv[1]
    
    with open(filename, 'r') as file:
        lines = file.readlines()
        
    for line in lines:
        line = line.strip()
        
        if line:
            words = line.split()
            
            for word in words:
                if word not in ['\n', '\t']:
                    words.remove(word)
            
            file.seek(0)
            file.writelines(lines)
            
    file.close()
    
    print("Done.")

