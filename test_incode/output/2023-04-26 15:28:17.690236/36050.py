#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a list of numbers and adds a list of words. """    
    port = int(sys.argv[1])
    
    words = []
    numbers = []
    
    # Start a server
    httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    # Start a thread to handle requests
    httpd.serve_forever()
    
    # Stop the server
    httpd.server_close()
    
    # Return the list of numbers and words
    return numbers, words
    
