#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of numbers. """    
    import sys
    port = int(sys.argv[1])
    
    numbers = []
    for arg in sys.argv[2:]:
        numbers.append(int(arg))
    
    numbers = list(set(numbers))
    numbers.sort()
    
    numbers_str = ','.join(str(x) for x in numbers)
    
    sys.stdout.write("Content-Type: text/html\n")
    sys.stdout.write("<html><body>\n")
    sys.stdout.write("<H1>Numbers</H1>\n")
    sys.stdout.write("<H2>%s</H2>\n" % numbers_str)
    sys.stdout.write("</body></html>\n")
    
    sys.stdout.flush()
    
    httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
    httpd.serve_forever()
    
