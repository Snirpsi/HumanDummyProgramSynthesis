#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes numbers or enumerates a list of words. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: %s <words>" % sys.argv[0])
        sys.exit()
    
    words = sys.argv[1:]
    
    words = [w.strip() for w in words]
    
    words.sort()
    
    sys.stdout.write("<html><body>")
    
    for word in words:
        sys.stdout.write("<hr>\n")
        sys.stdout.write("<i>%s</i>" % word)
        sys.stdout.write("<hr>\n")
    
    sys.stdout.write("</body></html>")
    
    sys.stdout.flush()
    
    
