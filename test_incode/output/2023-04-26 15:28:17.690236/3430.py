#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates words or opens user input. """    
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('localhost', port), MyHandler)
    httpd.serve_forever()
    
