#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens words and prints a port. """    
    import sys
    port = int(sys.argv[1])
    
    httpd = HTTPServer(("", port), WordsHandler)
    print("Starting web server on port " + str(port))
    httpd.serve_forever()

<|/ file filename=word