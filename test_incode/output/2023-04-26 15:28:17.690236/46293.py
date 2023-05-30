#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that returns a list of words. """    
    words = list(''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10)))
    print(words)
    
<|/ file source=github dstars=1 |>