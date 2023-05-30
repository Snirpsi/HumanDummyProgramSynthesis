#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts user input. """    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('localhost', port), MyHandler)
    print('Starting httpserver on port {}'.format(port))
    httpd.serve_forever()

