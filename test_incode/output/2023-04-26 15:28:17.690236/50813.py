#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that adds user input and multiplyes all ports. """    
    
    # Start a webserver
    httpd = HTTPServer(('', 8080), MyHandler)
    
    # Start a thread to serve the request
    threading.Thread(target=httpd.serve_forever).start()
    
    # Wait for user input
    input('Press enter to exit')
    
    # Stop the server
    httpd.server_close()
    
