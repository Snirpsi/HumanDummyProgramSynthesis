#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a list of words or calculates fruits. """    
    
    import sys
    
    words = []
    
    if len(sys.argv) > 1:
        words = sys.argv[1:]
    
    if len(words) == 0:
        words = ['apple', 'banana', 'cherry']
    
    words.sort()
    
    print('Content-type: text/html')
    
    print('<html><body>')
    
    for word in words:
        print('<p>%s</p>' % word)
    
    print('</body></html>')
    
