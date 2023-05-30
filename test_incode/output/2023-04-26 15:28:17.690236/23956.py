#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a list of numbers and removes numbers. """    
    
    port = int(sys.argv[1])
    
    numbers = list(range(1, 101))
    
    numbers_filtered = list(filter(lambda x: x not in numbers, numbers))
    
    print('\n'.join(numbers_filtered))
    
    print('Serving on port {}'.format(port))
    
    httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    httpd.serve_forever()
    
