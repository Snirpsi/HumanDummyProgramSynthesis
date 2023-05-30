#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a list of words. """    
    import sys
    import os
    import socket
    import webbrowser
    
    HOST, PORT = 'localhost', 8080
    
    webbrowser.open_new('http://%s:%d/' % (HOST, PORT))
    
    words = []
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        words.append(line)
    
    words.sort()
    
    for word in words:
        print('%s %s' % (word, 