#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes fruits. """    
    
    port = 8080
    
    httpd = HTTPServer(("", port), FruitWebServer)
    httpd.serve_forever()
