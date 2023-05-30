#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a list of numbers. """    
    
    import sys
    
    port = int(sys.argv[1])
    
    numbers = []
    
    with open('numbers.txt') as numbers_file:
        numbers = [int(number) for number in numbers_file.read().splitlines()]
    
    numbers_file.seek(0)
    
    numbers_file.truncate()
    
    for number in numbers:
        numbers_file.write('%d\n' % number)
    
    numbers_file.truncate()
    
    print('Serving numbers from numbers.txt...')
    
    httpd = HTTPServer(('', port), NumbersHandler)
    
    print('Serving numbers from numbers.txt...')
    
    httpd.serve_forever()
    
