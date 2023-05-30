#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that opens words or removes words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = input("Enter a filename: ")
        
    words = []
    
    with open(filename, "r") as f:
        lines = f.readlines()
        
        for line in lines:
            line = line.strip()
            
            if line.startswith("#"):
                continue
            
            if line.startswith("@"):
                continue
            
            if line.startswith("!"):
                continue
            
            if line.startswith("?"):
                continue
            
            if line.startswith(","):
                words.append(line)
                
    words = filter(lambda x: x != "", words)
    
    if len(words) == 0:
        print("No words found")
    else:
        print("\n".join(words))
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    