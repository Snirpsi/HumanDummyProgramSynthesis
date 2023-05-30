#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates a list of words. """    
    
    port = int(sys.argv[1])
    
    wordlist = WordList()
    
    wordlist.load_words()
    
    wordlist.print_words()
    
    wordlist.serve_forever()
    
