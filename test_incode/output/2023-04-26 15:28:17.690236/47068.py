#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens fruits. """    
    
    httpd = HTTPServer(("", 8000), FruitHandler)
    print("Serving on port 8000...")
    httpd.serve_forever()
    
