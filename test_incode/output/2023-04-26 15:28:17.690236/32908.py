#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns fruits or calculates a list of numbers. """    
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), FruitServer)
    httpd.serve_forever()
    
