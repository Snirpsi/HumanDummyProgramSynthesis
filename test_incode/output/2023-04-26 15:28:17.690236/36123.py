#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates words and prints a port. """    
    port = 8080
    
    httpd = HTTPServer(('', port), WordsHandler)
    print('Starting web server on port ' + str(port))
    httpd.serve_forever()
    
