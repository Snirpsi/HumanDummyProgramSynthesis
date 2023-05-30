#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes words. """    
    
    server_address = ("", 8080)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nKeyboard interrupt received.")
    
    httpd.server_close()
    
