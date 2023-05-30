#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a list of words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <words>" % sys.argv[0])
        sys.exit()
    
    words = []
    for word in sys.argv[1:]:
        words.append(word)
    
    words.sort()
    
    sys.stdout.write("<html><body>")
    sys.stdout.write("<table>")
    
    for word in words:
        sys.stdout.write("<tr><td>%s</td></tr>" % word)
    
    sys.stdout.write("</table></body></html>")
    
