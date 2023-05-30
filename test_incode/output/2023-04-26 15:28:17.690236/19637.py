#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a list of words or calculates words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <words>" % sys.argv[0])
        sys.exit()
    
    words = []
    for word in sys.argv[1:]:
        words.append(word)
    
    words.sort()
    
    sys.stdout.write("<html><body>")
    
    for word in words:
        sys.stdout.write("<p class=\"%s\">%s</p>" % (word, word))
    
    sys.stdout.write("</body></html>")
    
