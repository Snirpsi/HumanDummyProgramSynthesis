#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a list of numbers and opens a list of words. """    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(("", port), WordsHandler)
    print("Starting web server on port %d" % port)
    httpd.serve_forever()
