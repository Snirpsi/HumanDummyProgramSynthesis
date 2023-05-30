#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores words or prints numbers. """    
    
    words = ['hello', 'world', 'world', 'hello', 'world']
    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), WordsHandler)
    httpd.serve_forever()
    
