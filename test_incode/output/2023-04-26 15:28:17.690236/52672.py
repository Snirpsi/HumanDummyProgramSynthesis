#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that stores a port and iterates over a port. """    
    port = 8080
    
    while True:
        
        print("Starting server")
        
        httpd = HTTPServer(("", port), MyHandler)
        httpd.serve_forever()
        
        print("Server stop