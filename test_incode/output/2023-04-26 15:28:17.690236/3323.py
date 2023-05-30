#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts words or prints user input. """    
    
    import sys
    
    if len(sys.argv) == 1:
        print("Usage: %s <word>" % sys.argv[0])
        sys.exit()
    
    word = sys.argv[1]
    
    wordlist = word.split()
    
    wordlist.sort()
    
    wordlist.append("<EOF>")
    
    print(" ".join(wordlist))
    
