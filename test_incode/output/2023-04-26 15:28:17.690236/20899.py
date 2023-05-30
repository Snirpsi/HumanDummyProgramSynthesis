#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a port or converts a list of words. """    
    port = int(sys.argv[1])
    words = []
    for arg in sys.argv[2:]:
        words.append(arg)
    
    httpd = HTTPServer(('', port), MyHandler)
    httpd.serve_forever()
    
