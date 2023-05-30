#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that calculates words. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: python3 wordcount.py <wordlist>")
        exit(1)
    
    wordlist = sys.argv[1]
    
    wordcount = {}
    
    with open(wordlist) as f:
        for line in f:
            line = line.strip()
            
            if line == '':
                continue
            
            word, count = line.split('\t')
            
            wordcount[word] = int(count)
    
    wordcounts = sorted(wordcount.items(), key=lambda x: x[1], reverse=True)
    
    for word, count in wordcounts:
        print("%s: %d" % (word, count))
        
