#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns words or returns a list of words. """    
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == 'words':
        words = []
        for word in sys.stdin:
            word = word.strip()
            if word:
                words.append(word)
        print(words)
    else:
        words = sys.stdin.read().split()
        print(words)

<|/ file ext=.py filename=wordlist.py |>