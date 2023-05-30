#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens words. """    
    httpd = HTTPServer(('', 80), WordsHandler)
    print('Starting webserver on port 80')
    httpd.serve_forever()
