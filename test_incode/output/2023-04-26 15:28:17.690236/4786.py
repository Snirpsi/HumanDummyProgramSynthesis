#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes numbers and enumerates words. """    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: python wordcount.py <wordlist>")
        sys.exit()
    
    wordlist = sys.argv[1]
    
    wordcount = {}
    
    for word in wordlist.split():
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1
    
    for word in sorted(wordcount, key=wordcount.get, reverse=True):
        print("%s: %d" % (word, wordcount[word]))
    
