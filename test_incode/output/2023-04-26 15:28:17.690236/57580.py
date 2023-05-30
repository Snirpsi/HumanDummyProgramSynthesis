#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a list of numbers or removes numbers. """    
    port = int(sys.argv[1])
    httpd = HTTPServer(('', port), NumbersHandler)
    httpd.serve_forever()
