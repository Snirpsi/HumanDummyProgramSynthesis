#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns user input or converts a list of words. """    
    
    import sys
    
    if len(sys.argv) > 1:
        words = sys.argv[1:]
    else:
        words = []
    
    words = [word.lower() for word in words]
    
    if words == []:
        print("Please specify at least one word.")
    else:
        print("\n".join(words))

<|/ file ext=.py |>