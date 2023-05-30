#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns words. """    
    while True:
        words = words_from_file(sys.argv[1])
        if len(words) == 0:
            break
        sys.stdout.write(" ".join(words))
        sys.stdout.flush()
        
    
<|/ file filename=words_from_file.py |>