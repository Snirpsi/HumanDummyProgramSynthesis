#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of words. """    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s <words>' % sys.argv[0])
        sys.exit(1)
    
    words = []
    for line in sys.stdin:
        line = line.strip()
        if line == '':
            continue
        words.append(line)
    
    words.sort()
    
    print('<html><head><title>Words</title></head><body>')
    print('<table>')
    for word in words:
        print('<tr><td>%s</td></tr>' % word)
    print('</table></body></html>')

<|/ file filename=wordlist.py ext=.py |>