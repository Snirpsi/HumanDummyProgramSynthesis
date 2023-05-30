#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens words. """    
    httpd = HTTPServer(('localhost', 8000), WordsHandler)
    print('Starting httpd on port 8000')
    httpd.serve_forever()
    
