#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a list of numbers or enumerates a list of words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <words>" % sys.argv[0])
        sys.exit()
    
    words = sys.argv[1:]
    
    if len(words) == 0:
        print("Usage: %s <words>" % sys.argv[0])
        sys.exit()
    
    words = [w.strip() for w in words]
    
    words.sort()
    
    sys.stdout.write("<html><body>")
    
    for word in words:
        sys.stdout.write("<hr>\n")
        sys.stdout.write("<center>%s</center>\n" % word)
        sys.stdout.write("<hr>\n")
    
    sys.stdout.write("</body></html>")
    
    sys.stdout.flush()
    
    