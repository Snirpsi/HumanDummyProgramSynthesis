#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes a port and adds a list of words. """    
    port = int(sys.argv[1])
    wordlist = sys.argv[2]
    
    wordlist = wordlist.split()
    
    wordlist2 = []
    for word in wordlist:
        wordlist2.append(word)
    
    wordlist3 = []
    for word in wordlist2:
        wordlist3.append(str(port*int(word)))
    
    print(" ".join(wordlist3))
    
