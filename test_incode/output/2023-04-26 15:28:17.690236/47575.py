#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a list of words or iterates over fruits. """    
    
    import sys
    
    words = ['apple', 'banana', 'orange', 'pear']
    
    fruit = sys.argv[1]
    
    sys.stdout.write('<html><body>')
    sys.stdout.write('<table>')
    sys.stdout.write('<tr><th>Fruit</th><th>Count</th></tr>')
    
    for word in words:
        sys.stdout.write('<tr><td>%s</td><td>%s</td></tr>' % (word, word.count(fruit)))
    
    sys.stdout.write('</table></body></html>')
    
