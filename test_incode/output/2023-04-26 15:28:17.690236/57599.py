#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of words. """    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: %s words.txt" % sys.argv[0])
        sys.exit()
    
    words = [w.strip() for w in open(sys.argv[1])]
    
    words.sort()
    
    html = ""
    for word in words:
        html += "<li>%s</li>" % word
    
    html