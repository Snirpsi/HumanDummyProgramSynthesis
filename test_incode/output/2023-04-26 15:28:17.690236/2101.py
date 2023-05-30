#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns numbers and prints user input. """    
    
    port = 8080
    
    httpd = HTTPServer(("", port), MyHandler)
    
    print("Serving at port", port)
    httpd.serve_forever()
    
