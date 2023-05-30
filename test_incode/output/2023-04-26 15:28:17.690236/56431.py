#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns user input and removes words. """    
    
    # Start a web server
    webserver = HTTPServer(('', 80), MyHandler)
    webserver.serve_forever()
    
    # 