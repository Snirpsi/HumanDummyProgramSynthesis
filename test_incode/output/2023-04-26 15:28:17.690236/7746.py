#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes words. """    
    
    # Start a web server
    httpd = HTTPServer(('', 8080), SimpleHTTPRequestHandler)
    
    # Start a thread to handle requests
    threading.Thread(target=httpd.serve_forever).start()
    
    # Wait forever
    httpd.serve_forever()
    
    # Stop the server
    httpd.server_close()
    
