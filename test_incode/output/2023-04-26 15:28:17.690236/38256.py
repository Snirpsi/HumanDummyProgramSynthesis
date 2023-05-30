#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds numbers or calculates fruits. """    
    
    port = 8080
    
    httpd = HTTPServer(("", port), FruitServer)
    httpd.serve_forever()
