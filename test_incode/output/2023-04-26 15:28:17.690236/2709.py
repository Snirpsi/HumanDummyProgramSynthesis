#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints user input or opens words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = "words.txt"
        
    with open(filename) as f:
        words = [line.strip() for line in f]
    
    words.sort()
    
    print("\n".join(words))
    
    if len(sys.argv) > 2:
        filename = sys.argv[2]
    else:
        filename = "words.txt"
        
    with open(filename) as f:
        words = [line.strip() for line in f]
    
    words.sort()
    
    print("\n".join(words))
    
    if len(sys.argv) > 3:
        filename = sys.argv[3]
    else:
        filename = "words.txt"
        
    with open(filename) as f:
        words = [line.strip() for line in f]
    
    words.sort()
    
    print("\n".join(words))
    
    if len(sys.argv) > 4:
        filename = sys.argv[4]
    else:
        filename = "words.txt"
        
    with open(filename) as f:
        words = [line.strip() for line in f]
    
    words.sort()
    
    print("\n".join(words))
    
    if len(sys.argv) > 5:
        filename = sys.argv[5]
    else:
        filename = "words.txt"
        
    with open(filename) as f:
        words = [line.strip() for line in f]
    
    words.sort()
    
    print("\n".join(words))
    
    if len(sys.argv) > 6:
        filename = sys.argv[6]
    else:
        filename = "words.txt"
        
    with open(filename) as f:
        words = [line.strip() for line in f]
    
    words.sort()
    
    print("\n".join(words))
    
    if len(sys.argv) > 7:
        filename = sys.argv[7]
    else:
        filename = "words.txt"
        
    with open(filename) as f:
        words = [line.strip() for line in f]
    
    words.sort()
    
    print("\n".join(words))
    
    if len(sys.argv) > 8:
        filename = sys.argv[8]
    else:
        filename = "words.txt"
        
    with open(filename) as f:
        words = [line.strip() for line in f]
    
    words.sort()
    
    print("\n".join(words))
    
    if len(sys.argv) > 9:
        filename = sys.argv[9]
    else:
        filename = "words.txt"
        
    with open(filename) as f:
        words = [line.strip() for line in f]
    
    words.sort()
    
    print("\n".join(words))
    
    if len(sys.argv) > 10:
        filename = sys.argv[10]
    else:
        filename = "words.txt"
        
    with open(filename) as f:
        words = [line.strip() for line in f]
    
    words.sort()
    
    print("\n".join(words))
    
    if len(sys.argv) > 11:
        filename = sys.argv[11]
    else:
        filename = "words.txt"
        