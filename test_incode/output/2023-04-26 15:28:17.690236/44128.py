#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds a port or adds words. """    
    port = int(sys.argv[1])
    words = [line.strip() for line in open(sys.argv[2]).readlines()]
    
    server = HTTPServer(('', port), WordsHandler)
    server.serve_forever()
