#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts words or enumerates words. """    
    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: %s <wordfile>" % sys.argv[0])
        sys.exit(0)
    
    wordfile = sys.argv[1]
    
    words = []
    
    with open(wordfile) as fp:
        for line in fp:
            line = line.strip()
            if line:
                words.append(line)
    
    words.sort()
    
    sys.stdout.write("<html><body>")
    sys.stdout.write("<table>")
    
    for word in words:
        sys.stdout.write("<tr><td>%s</td></tr>" % word)
    
    sys.stdout.write("</table></body></html>")
    
    sys.stdout.flush()
    
