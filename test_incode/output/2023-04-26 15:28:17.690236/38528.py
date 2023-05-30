#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of words. """    
    
    import sys
    
    words = []
    for arg in sys.argv[1:]:
        words.append(arg.strip())
    
    words.sort()
    
    html = ''
    for word in words:
        html += '<p> %s </p>\n' % word
    
    sys.stdout.write(html)
    
