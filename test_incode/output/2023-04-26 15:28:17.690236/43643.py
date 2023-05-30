#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of words. """    
    import sys
    import os
    import webbrowser
    
    port = int(sys.argv[1])
    
    words = []
    for arg in sys.argv[2:]:
        words.append(arg.strip())
    
    words.sort()
    
    webbrowser.open_new("http://localhost:%d/" % port)
    
    for word in words:
        print("%s -> %s" % (word, 