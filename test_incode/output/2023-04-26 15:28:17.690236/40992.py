#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a list of words or enumerates numbers. """    
    
    import sys
    
    if len(sys.argv) > 1:
        words = sys.argv[1:]
    else:
        words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    words.sort()
    
    print('<html><body>')
    for word in words:
        print('<p>%s</p>' % word)
    print('</body></html>')
    
    

<|/ file ext=.py source=github |>