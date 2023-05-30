#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds words and prints a port. """    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: %s <word>" % sys.argv[0])
        sys.exit()
    
    word = sys.argv[1]
    
    port = ""
    
    for i in range(len(word)):
        port += word[i]
        
        if i < len(word)-1:
            port += " "
    
    print(port)
    
