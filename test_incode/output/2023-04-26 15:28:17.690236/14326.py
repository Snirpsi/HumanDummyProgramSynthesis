#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a port or removes a list of numbers. """    
    port = int(sys.argv[1])
    if len(sys.argv) > 2:
        numbers = sys.argv[2:]
    else:
        numbers = []
    
    httpd = HTTPServer(("", port), MyHandler)
    httpd.serve_forever()
