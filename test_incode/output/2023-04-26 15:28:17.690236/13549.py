#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes a list of words. """    
    
    words = ["Hello", "World", "!"]
    
    httpd = HTTPServer(('', 8080), MyHandler)
    httpd.serve_forever()
    
