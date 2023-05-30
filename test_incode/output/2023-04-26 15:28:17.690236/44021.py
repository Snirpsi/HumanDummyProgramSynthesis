#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts numbers. """    
    import sys
    if len(sys.argv) < 2:
        print("Usage: python3 number_to_word.py number")
        sys.exit()
    number = sys.argv[1]
    word = number_to_word(number)
    print(word)

<|/ file ext=.py source=github |>