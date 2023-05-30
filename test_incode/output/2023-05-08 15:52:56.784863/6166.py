#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A minimal webserver that requests a list of words.
    #The server will respond with a list of all words in the given language.
    import sys
    import os
    sys.path.append(os.getcwd())
    from wordlist import Wordlist
    wordlist = Wordlist(sys.argv[1])
    wordlist.print_words()

