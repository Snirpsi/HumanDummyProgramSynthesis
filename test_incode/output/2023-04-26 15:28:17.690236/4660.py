#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a list of words and returns a port. """    
    
    words = []
    port = 5000
    
    # Create a server and bind it to the specified port
    httpd = HTTPServer(('', port), WordsHandler)
    
    # Start the server
    httpd.serve_forever()
    
    # Stop the server
    httpd.shutdown()
    
    # 