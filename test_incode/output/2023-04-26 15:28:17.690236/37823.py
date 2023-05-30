#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a list of words or opens all ports. """    
    import sys
    port = int(sys.argv[1])
    
    words = []
    
    for arg in sys.argv[2:]:
        words.append(arg.strip())
    
    words.sort()
    
    ports = [port for port in range(65535) if port not in words]
    
    for port in ports:
        
        httpd = HTTPServer(('', port), Handler)
        
        print('Starting httpd on port %s' % port)
        
        httpd.serve_forever()
        
