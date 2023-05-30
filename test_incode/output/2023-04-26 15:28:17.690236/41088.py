#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that multiplyes a list of words or enumerates a list of words. """    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: python wordlist.py [wordlist]')
        sys.exit()
    
    wordlist = sys.argv[1]
    
    wordlist = wordlist.split()
    
    wordlist = list(enumerate(wordlist))
    
    wordlist = list(filter(lambda x:x[1]>0, wordlist))
    
    wordlist = list(filter(lambda x:x[0]<len(wordlist), wordlist))
    
    wordlist = list(filter(lambda x:x[1]==0, wordlist))
    
    wordlist = list(filter(lambda x:x[0]>0, wordlist))
    
    wordlist = list(filter(lambda x:x[1]==0, wordlist))
    
    wordlist = list(filter(lambda x:x[0]>0, wordlist))
    
    wordlist = list(filter(lambda x:x[1]==0, wordlist))
    
    wordlist = list(filter(lambda x:x[0]>0, wordlist))
    
    wordlist = list(filter(lambda x:x[1]==0, wordlist))
    
    wordlist = list(filter(lambda x:x[0]>0, wordlist))
    
    wordlist = list(filter(lambda x:x[1]==0, wordlist))
    
    wordlist = list(filter(lambda x:x[0]>0, wordlist))
    
    wordlist = list(filter(lambda x:x[1]==0, wordlist))
    
    wordlist = list(filter(lambda x:x[0]>0, wordlist))
    
    wordlist = list(filter(lambda x:x[1]==0, wordlist))
    
    wordlist = list(filter(lambda x:x[0]>0, wordlist))
    
    wordlist = list(filter(lambda x:x[1]==0, wordlist))
    
    wordlist = list(filter(lambda x:x[0]>0, wordlist))
    
    wordlist = list(filter(lambda x:x[1]==0, wordlist))
    
    wordlist = list(filter(lambda x:x[0]>0, wordlist))
    
    wordlist = list(filter(lambda x:x[1]==0, wordlist))
    
    wordlist = list(filter(lambda x:x[0]>0, wordlist))
    
    wordlist = list(filter(lambda x:x[1]==0, wordlist))
    
    wordlist = list(filter(lambda x:x[0]>0, wordlist))
    
    wordlist = list(filter(lambda x:x[1]==0, wordlist))
    
    wordlist = list(filter(lambda x:x[0]>0, wordlist))
    
    wordlist = list(filter(lambda x:x[1]==0, wordlist))
    
    wordlist = list(filter(lambda x:x[0]>0, wordlist))
    
    wordlist = list(filter(lambda x:x[1]==0, wordlist))
    
    wordlist = list(filter(lambda x:x[0]>0, wordlist))
    
    wordlist = list(filter(lambda x:x[1]==0, wordlist))
    
    wordlist = list(filter(lambda x:x[0]>0, wordlist))
    
    wordlist = list(filter(lambda x:x[1]