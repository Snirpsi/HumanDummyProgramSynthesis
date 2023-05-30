#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts words or calculates a list of words. """    
    
    # Start a webserver
    httpd = HTTPServer(('', 80), WordsHandler)
    
    # Start a thread to handle requests
    threading.Thread(target=httpd.serve_forever).start()
    
    # Wait forever
    httpd.serve_forever()
    
    # Stop the webserver
    httpd.shutdown()
    
    # Stop the thread
    httpd.server_