#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints numbers and multiplyes user input. """    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), MyHandler)
    httpd.serve_forever()
    
