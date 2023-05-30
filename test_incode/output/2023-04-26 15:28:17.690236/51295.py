#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns user input. """    
    
    port = 8080
    
    server = HTTPServer(('', port), MyHandler)
    
    server.serve_forever()
    
