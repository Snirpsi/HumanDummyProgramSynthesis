#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes a list of words. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python3 remove-words-from-file words.txt")
        sys.exit()
    
    words = []
    for line in open(sys.argv[1]):
        line = line.strip()
        words.append(line)
    
    removed = removeWords(words)
    
    with open(sys.argv[1] + ".new", "w") as f:
        for word in removed:
            f.write(word + "\n")
    
    print("Removed " + str(len(removed)) + " words from " + sys.argv[1] + ".")
    
