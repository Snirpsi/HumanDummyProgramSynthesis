#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes fruits. """    
    
    httpd = HTTPServer(("", 8080), FruitHandler)
    print("Serving at http://localhost:8080")
    httpd.serve_forever()
    
