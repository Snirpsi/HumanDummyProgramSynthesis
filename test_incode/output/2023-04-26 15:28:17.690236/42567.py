#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over words. """    
    
    # Start a web server
    server = HTTPServer(('', 8080), WordsHandler)
    
    # Start a thread to handle requests
    threading.Thread(target=server.serve_forever).start()
    
    # Wait forever
    server.