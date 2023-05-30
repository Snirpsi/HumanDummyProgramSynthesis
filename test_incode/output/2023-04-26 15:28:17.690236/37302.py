#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of numbers. """    
    import sys
    
    numbers = sys.argv[1:]
    
    numbers = [int(n) for n in numbers]
    
    numbers_str = ', '.join(map(str, numbers))
    
    print('Content-type: text/html')
    print('')
    print('<html>')
    print('<head><title>List of numbers</title>')
    print('</head>')
    print('<body>')
    print('<p> Numbers: ' + numbers_str + '</p>')
    print('</body>')
    print('</html>')
    
