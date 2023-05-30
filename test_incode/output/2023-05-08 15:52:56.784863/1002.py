#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A minimal webserver that calculates a list of words.
    #It can be run from the command line with python wordlist.py
    #or it can be run from the web interface with http://127.0.0.1:8000/wordlist.py
    #It will print out the words in the list to the terminal.
    import sys
    wordlist = sys.argv[1:]
    for word in wordlist:
        print(word)
    print("Done.")

