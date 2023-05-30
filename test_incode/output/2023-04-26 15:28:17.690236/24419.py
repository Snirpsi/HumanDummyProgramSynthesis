#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that removes a list of words and converts fruits. """    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: %s <fruits>" % sys.argv[0])
        sys.exit()
    
    fruits = sys.argv[1].split()
    
    remove_fruits(fruits)
    
    print("Done")

<|/ file filename=remove_words.py source=github |>