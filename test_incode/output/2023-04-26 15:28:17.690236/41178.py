#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts numbers and enumerates a list of words. """    
    
    # Start a web server
    httpd = HTTPServer(('', 8080), RequestHandler)
    
    # Start a thread that serves forever
    threading.Thread(target=httpd.serve_forever).start()
    
    # Wait forever
    httpd.