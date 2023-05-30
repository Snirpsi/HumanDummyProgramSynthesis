#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that calculates words. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: python wordcount.py <input>")
        sys.exit()
    
    file = sys.argv[1]
    
    words = file.split()
    
    counts = {}
    
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    
    for word in counts:
        print(word, counts[word])
    
