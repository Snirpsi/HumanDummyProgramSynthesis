#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts a list of words or converts a port. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python3 wordlist.py <wordlist>")
        sys.exit()
    
    wordlist = sys.argv[1]
    
    words = wordlist.split()
    
    ports = []
    
    for word in words:
        ports.append(int(word))
    
    ports.sort()
    
    print("\n".join(map(str, ports)))
    
