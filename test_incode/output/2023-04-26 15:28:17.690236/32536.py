#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts a port or removes words. """    
    
    # Start a web server
    httpd = HTTPServer(('', PORT), SimpleHTTPRequestHandler)
    
    # Start a thread to serve requests
    threading.Thread(target=httpd.serve_forever).start()
    
    # Wait until CTRL-C is pressed
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        httpd.shutdown()
        httpd.server_close()
        
