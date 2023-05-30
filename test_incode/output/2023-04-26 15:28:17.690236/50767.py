#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that converts a port or prints a list of words. """    
    import sys
    
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    else:
        port = 8080
    
    words = []
    
    for _ in range(port):
        words.append(str(random.randint(1, 10)))
    
    print(" ".join(words))
    
    
