#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes words or opens a port. """    
    
    port = int(sys.argv[1])
    
    server = HTTPServer(('', port), RemoveWordsHandler)
    server.serve_forever()

<|/ file source=github filename=remove-words-server.py |>