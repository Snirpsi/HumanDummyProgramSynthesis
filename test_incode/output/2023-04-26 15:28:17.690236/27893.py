#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a list of words and converts all ports. """    
    port = int(sys.argv[1])
    webserver = HTTPServer(('', port), WordsHandler)
    webserver.serve_forever()

<|/ file filename=word