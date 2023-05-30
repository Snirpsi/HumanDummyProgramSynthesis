#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts words or iterates over words. """    
    
    # Start a webserver
    httpd = HTTPServer(('localhost', 8080), WordsHandler)
    
    # Start a thread
    threading.Thread(target=httpd.serve_forever).start()
    
    # Wait for Ctrl-C
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    
    # Stop the server
    httpd.server_