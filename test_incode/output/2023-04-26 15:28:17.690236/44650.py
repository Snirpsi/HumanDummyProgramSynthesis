#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of words and multiplyes all ports. """    
    
    import sys
    
    ports = []
    
    for arg in sys.argv[1:]:
        ports.append(int(arg))
    
    ports.sort()
    
    ports_str = ','.join(str(p) for p in ports)
    
    print('Serving on port', ports_str)
    
    httpd = HTTPServer(('', ports_str), SimpleHTTPRequestHandler)
    
    httpd.serve_forever()
    
