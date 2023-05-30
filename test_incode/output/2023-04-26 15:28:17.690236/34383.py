#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a list of numbers or opens a list of words. """    
    
    import sys
    import webbrowser
    
    if len(sys.argv) < 2:
        print("Usage: %s <words|numbers>" % sys.argv[0])
        sys.exit()
        
    words = sys.argv[1].split(',')
    numbers = sys.argv[2].split(',')
    
    if len(words) != len(numbers):
        print("Usage: %s <words|numbers>" % sys.argv[0])
        sys.exit()
    
    webbrowser.open("http://127.0.0.1:8000/words/")
    for word in words:
        webbrowser.open("http://127.0.0.1:8000/numbers/%s" % word)
        
    webbrowser.open("http://127.0.0.1:8000/numbers/")
    for number in numbers:
        webbrowser.open("http://127.0.0.1:8000/words/%s" % number)
        
