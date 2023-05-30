#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts words. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s words.txt" % sys.argv[0])
        sys.exit()
    
    words = []
    for line in open(sys.argv[1]):
        words.append(line.strip())
    
    words.sort()
    
    html = ""
    for word in words:
        html += "<li>%s</li>" % word
    
    html