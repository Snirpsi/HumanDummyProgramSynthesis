#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a list of numbers. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    numbers = []
    
    for x in range(port):
        numbers.append(x)
        
    numbers_str = ','.join(str(x) for x in numbers)
    
    print('Content-type: text/html')
    print('')
    print('<html><body>')
    print('<p>Numbers: %s' % numbers_str)
    print('</body></html>')
    
