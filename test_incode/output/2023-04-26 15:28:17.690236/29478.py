#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that enumerates a list of words or converts user input. """    
    
    import sys
    
    if len(sys.argv) > 1:
        word = sys.argv[1]
    else:
        word = input("Enter a word: ")
    
    wordlist = word.split()
    
    print("\n".join("%s: %s" % (word, wordlist[i]) for i in range(len(wordlist))))
    
