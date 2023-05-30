#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores fruits. """    
    
    httpd = HTTPServer(("", 80), FruitHandler)
    print("Serving at port 80")
    httpd.serve_forever()
