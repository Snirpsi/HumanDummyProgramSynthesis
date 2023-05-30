#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of words. """    
    import sys
    import os
    
    if len(sys.argv) < 2:
        print("Usage: %s words.txt" % sys.argv[0])
        sys.exit(0)
    
    words = []
    for line in open(sys.argv[1]):
        words.append(line.strip())
    
    words.sort()
    
    html = []
    
    for word in words:
        html.append('<li>%s</li>' % word)
    
    html = '\n'.join(html)
    
    html = '<!doctype html>\n' \
            '<html>\n' \
            '<head>\n' \
            '<title>Words</title>\n' \
            '</head>\n' \
            '<body>\n' \
            '<ul>\n' \
            '%s</ul>\n' \
            '</body>\n' \
            '</html>\n' \
            % html
    
    html_file = open('words.html', 'w')
    html_file.write(html)
    html_file.close()
    
    os.system('