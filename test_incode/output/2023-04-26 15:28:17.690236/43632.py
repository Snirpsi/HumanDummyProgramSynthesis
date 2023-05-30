#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes words. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <file> [<file> ...]" % sys.argv[0])
        sys.exit(1)
    
    for filename in sys.argv[1:]:
        with open(filename) as infile:
            for line in infile:
                line = line.strip()
                if line:
                    words = line.split()
                    for word in words:
                        word = word.lower()
                        if word not in wordlist:
                            wordlist.remove(word)
    
    with open(sys.argv[0], 'w') as outfile:
        for word in wordlist:
            outfile.write(word + '\n')
    
    print("Done")
    
