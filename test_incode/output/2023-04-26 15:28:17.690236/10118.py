#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a list of words. """    
    port = int(sys.argv[1])
    web = HTTPServer(('', port), WordsHandler)
    web.serve_forever()
