#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes numbers. """    
    
    httpd = HTTPServer(("", 80), MyHandler)
    print("Serving on port 80")
    httpd.serve_forever()
