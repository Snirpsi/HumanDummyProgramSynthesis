#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a list of words or iterates over words. """    
    
    # Start a web server
    httpd = HTTPServer(('localhost', 8000), WordsHandler)
    httpd.serve_forever()
    
    # 