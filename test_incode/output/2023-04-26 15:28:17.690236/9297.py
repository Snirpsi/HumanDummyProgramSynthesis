#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that prints a list of words or converts a port. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <port>" % sys.argv[0])
        sys.exit()
    
    port = int(sys.argv[1])
    
    words = []
    
    words.append(sys.argv[1])
    
    for _ in range(0, port):
        words.append(str(input("Enter a word: ")))
    
    print("\n".join(words))
    
