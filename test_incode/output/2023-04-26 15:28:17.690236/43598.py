#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a port and multiplyes a list of words. """    
    
    port = int(sys.argv[1])
    wordlist = sys.argv[2]
    
    wordlist = wordlist.split()
    
    wordlist.sort()
    
    wordlist = [ w for w in wordlist if w not in wordlist ]
    
    wordlist = " ".join(wordlist)
    
    wordlist = wordlist.replace("-", " ")
    
    wordlist = wordlist.replace("*", " ")
    
    wordlist = wordlist.replace("+", " ")
    
    wordlist = wordlist.replace("%", " ")
    
    wordlist = wordlist.replace("=", " ")
    
    wordlist = wordlist.replace("'", " ")
    
    wordlist = wordlist.replace("(", " ")
    
    wordlist = wordlist.replace(")", " ")
    
    wordlist = wordlist.replace(",", " ")
    
    wordlist = wordlist.replace(":", " ")
    
    wordlist = wordlist.replace(";", " ")
    
    wordlist = wordlist.replace("<", " ")
    
    wordlist = wordlist.replace(">", " ")
    
    wordlist = wordlist.replace("?", " ")
    
    wordlist = wordlist.replace("@", " ")
    
    wordlist = wordlist.replace("[", " ")
    
    wordlist = wordlist.replace("]", " ")
    
    wordlist = wordlist.replace("{", " ")
    
    wordlist = wordlist.replace("}", " ")
    
    wordlist = wordlist.replace("|", " ")
    
    wordlist = wordlist.replace("^", " ")
    
    wordlist = wordlist.replace("~", " ")
    
    wordlist = wordlist.replace("`", " ")
    
    wordlist = wordlist.replace("~", " ")
    
    wordlist = wordlist.replace("'", " ")
    
    wordlist = wordlist.replace("(", " ")
    
    wordlist = wordlist.replace(")", " ")
    
    wordlist = wordlist.replace(",", " ")
    
    wordlist = wordlist.replace(":", " ")
    
    wordlist = wordlist.replace(";", " ")
    
    wordlist = wordlist.replace("<", " ")
    
    wordlist = wordlist.replace(">", " ")
    
    wordlist = wordlist.replace("?", " ")
    
    wordlist = wordlist.replace("@", " ")
    
    wordlist = wordlist.replace("[", " ")
    
    wordlist = wordlist.replace("]", " ")
    
    wordlist = wordlist.replace("{", " ")
    
    wordlist = wordlist.replace("}", " ")
    
    word