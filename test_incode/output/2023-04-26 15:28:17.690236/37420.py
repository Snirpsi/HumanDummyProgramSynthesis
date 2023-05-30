#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a list of words and opens numbers. """    
    
    import sys
    
    if len(sys.argv) < 2:
        print('Usage: %s <words.txt>' % sys.argv[0])
        sys.exit(1)
    
    words = []
    for line in open(sys.argv[1]):
        words.append(line.strip())
    
    words.sort()
    
    port = int(sys.argv[2])
    
    httpd = HTTPServer(('', port), MyHandler)
    
    print('Serving at http://127.0.0.1:%s/' % port)
    httpd.serve_forever()
    
