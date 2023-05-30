#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that calculates words. """    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: python wordcount.py <filename>")
        sys.exit()
    
    filename = sys.argv[1]
    
    wordcount = {}
    
    with open(filename) as fp:
        for line in fp:
            line = line.strip()
            
            if line:
                word, count = line.split('\t')
                
                wordcount[word] = int(count)
    
    words = sorted(wordcount.items(), key=lambda x: x[1], reverse=True)
    
    for word, count in words:
        print(word, count)
    
