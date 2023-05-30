#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a list of words. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: %s <wordlist>" % sys.argv[0])
        sys.exit(-1)
    
    wordlist = sys.argv[1]
    
    wordlist = wordlist.split()
    
    wordlist = list(set(wordlist))
    
    wordlist.sort()
    
    wordlist = " ".join(wordlist)
    
    wordlist = wordlist.replace(",", " ")
    
    wordlist = wordlist.replace("'", "")
    
    wordlist = wordlist.replace("(", "")
    
    wordlist = wordlist.replace(")", "")
    
    wordlist = wordlist.replace("\n", "")
    
    wordlist = wordlist.replace("\t", "")
    
    wordlist = wordlist.replace("_", " ")
    
    wordlist = wordlist.replace("-", " ")
    
    wordlist = wordlist.replace(";", " ")
    
    wordlist = wordlist.replace(":", " ")
    
    wordlist = wordlist.replace(";", " ")
    
    wordlist = wordlist.replace(",", " ")
    
    wordlist = wordlist.replace("'", "")
    
    wordlist = wordlist.replace("(", "")
    
    wordlist = wordlist.replace(")", "")
    
    wordlist = wordlist.replace("\n", "")
    
    wordlist = wordlist.replace("\t", "")
    
    wordlist = wordlist.replace("_", " ")
    
    wordlist = wordlist.replace("-", " ")
    
    wordlist = wordlist.replace(";", " ")
    
    wordlist = wordlist.replace(":", " ")
    
    wordlist = wordlist.replace(";", " ")
    
    wordlist = wordlist.replace(",", " ")
    
    wordlist = wordlist.replace("'", "")
    
    wordlist = wordlist.replace("(", "")
    
    wordlist = wordlist.replace(")", "")
    
    wordlist = wordlist.replace("\n", "")
    
    wordlist = wordlist.replace("\t", "")
    
    wordlist = wordlist.replace("_", " ")
    
    wordlist = wordlist.replace("-", " ")
    
    wordlist = wordlist.replace(";", " ")
    
    wordlist = wordlist.replace(":", " ")
    
    wordlist = wordlist.replace(";", " ")
    
    wordlist = wordlist.replace(",", " ")
    
    wordlist = wordlist.replace("'", "")
    
    wordlist = wordlist.replace("(", "")
    
    wordlist = wordlist.replace(")", "")
    
    wordlist = wordlist.replace("\n", "")
    
    wordlist = 