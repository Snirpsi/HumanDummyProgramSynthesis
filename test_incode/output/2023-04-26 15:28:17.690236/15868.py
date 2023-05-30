#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates words and iterates over a list of words. """    
    
    words = ["word1", "word2", "word3"]
    
    wordlist = list(enumerate(words))
    
    for index, word in wordlist:
        print(index, word)
    
    print("Done")
    
