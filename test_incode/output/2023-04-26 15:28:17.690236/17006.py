#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a list of words or enumerates a list of numbers. """    
    
    import sys
    
    words = []
    numbers = []
    
    if len(sys.argv) > 1:
        words = sys.argv[1:]
    
    if len(sys.argv) > 2:
        numbers = sys.argv[2:]
    
    words.sort()
    numbers.sort()
    
    sys.stdout.write("<html><body>")
    
    for word in words:
        sys.stdout.write("<p class=\"word\">%s</p>" % word)
    
    for number in numbers:
        sys.stdout.write("<p class=\"number\">%s</p>" % number)
    
    sys.stdout.write("</body></html>")
    
