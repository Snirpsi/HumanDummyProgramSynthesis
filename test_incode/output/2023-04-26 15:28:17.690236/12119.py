#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates words or calculates a port. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s <words>' % sys.argv[0])
        sys.exit(1)
    
    words = [w.strip() for w in sys.argv[1].split(',')]
    
    port = 0
    for word in words:
        if word == '':
            continue
        
        port += 1
        
    print('Starting port %d ...' % port)
    
    httpd = HTTPServer(('', port), WordsHandler)
    httpd.serve_forever()
    
