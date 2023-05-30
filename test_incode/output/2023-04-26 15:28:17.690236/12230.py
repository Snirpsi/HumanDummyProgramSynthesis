#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens words or calculates a list of numbers. """    
    
    httpd = HTTPServer(('', 8000), WordsHandler)
    httpd.serve_forever()
    
