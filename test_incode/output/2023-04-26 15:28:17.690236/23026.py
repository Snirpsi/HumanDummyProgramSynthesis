#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints words and removes a list of numbers. """    
    port = int(sys.argv[1])
    
    httpd = HTTPServer(('', port), WordsHandler)
    httpd.serve_forever()

<|/ file filename=word