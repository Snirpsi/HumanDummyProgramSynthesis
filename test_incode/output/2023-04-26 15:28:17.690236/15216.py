#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts words or enumerates a port. """    
    import sys
    
    if len(sys.argv) == 1:
        print("Usage: python word.py <port>")
        exit()
    
    port = int(sys.argv[1])
    
    words = []
    
    with open('/etc/wordlist') as f:
        for line in f:
            line = line.strip()
            
            if line.startswith("#"):
                continue
            
            words.append(line)
    
    words.sort()
    
    word = ""
    
    for word in words:
        if word == "":
            word += port
        else:
            word += port
    
    print(word)
    
