#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a list of numbers and converts user input. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    numbers = []
    
    for number in range(1, port+1):
        numbers.append(str(number))
    
    numbers_str = ','.join(numbers)
    
    print('Content-type: text/html')
    print('')
    print('<html>')
    print('<head>')
    print('<title>Converting numbers to words</title>')
    print('</head>')
    print('<body>')
    print('<p>Numbers: ' + numbers_str + '</p>')
    print('</body>')
    print('</html>')
    
