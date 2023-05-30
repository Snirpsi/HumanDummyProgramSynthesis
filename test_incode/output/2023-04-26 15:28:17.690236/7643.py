#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates user input or opens a list of words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <words>" % sys.argv[0])
        sys.exit()
    
    words = sys.argv[1:]
    
    words = [word.strip() for word in words]
    
    words.sort()
    
    html = "<html><body>"
    
    for word in words:
        html += "<p>%s</p>" % word
    
    html += "</body></html>"
    
    sys.stdout.write(html)
    
