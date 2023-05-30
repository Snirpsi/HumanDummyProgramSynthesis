#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a list of numbers and stores fruits. """    
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(("", port), FruitServer)
    httpd.serve_forever()
