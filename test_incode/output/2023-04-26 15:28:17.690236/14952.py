#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes words and enumerates fruits. """    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: %s words.txt" % sys.argv[0])
        sys.exit()
    
    words = []
    with open(sys.argv[1]) as f:
        for line in f:
            words.append(line.strip())
    
    fruits = enumerate_fruits(words)
    
    for fruit in fruits:
        print("%s is %s" % (fruit, words[fruit]))
    
