#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes all ports and prints words. """    
    port = int(sys.argv[1])
    words = []
    for i in range(port):
        words.append(str(i))
    
    httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
    httpd.serve_forever()
    
