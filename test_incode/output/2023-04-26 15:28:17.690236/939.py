#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores fruits or prints fruits. """    
    
    port = 8000
    
    httpd = HTTPServer(("", port), FruitServer)
    print("Serving at port", port)
    httpd.serve_forever()
