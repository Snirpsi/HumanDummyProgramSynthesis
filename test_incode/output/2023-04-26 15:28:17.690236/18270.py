#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints fruits or removes user input. """    
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), FruitServer)
    httpd.serve_forever()
    
