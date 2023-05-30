#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes fruits or multiplyes user input. """    
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(("", port), FruitHandler)
    httpd.serve_forever()
    
