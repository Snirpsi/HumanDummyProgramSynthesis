#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds numbers or calculates a list of numbers. """    
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(("", port), MyHandler)
    httpd.serve_forever()
    
