#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that adds words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python addword.py <word>")
        sys.exit()
    
    word = sys.argv[1]
    
    print("Adding word: " + word)
    
    wordlist = open("wordlist.txt", "r")
    wordlist = wordlist.readlines()
    wordlist.close()
    
    wordlist.insert(0, word)
    
    wordlist = open("wordlist.txt", "w")
    wordlist.writelines(wordlist)
    
    wordlist.close()
    
    print("Done!")
    
