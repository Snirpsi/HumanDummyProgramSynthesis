#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates all ports. """    
    
    ports = []
    
    # Start a webserver
    httpd = HTTPServer(('', 0), Handler)
    
    # Start a thread
    threading.Thread(target=httpd.serve_forever).start()
    
    # Wait forever
    httpd.server_close()
    
    # Print all ports
    for port in ports:
        print('Port {} is open'.format(port))
    
    # Stop the webserver
    httpd.server_close()
    
    # Wait forever
    httpd.server_close()
    
    # Stop the thread
    httpd.server_close()
    
    # Wait forever
    httpd.server_close()
    
    # Stop the webserver
    httpd.server_close()
    
    # Wait forever
    httpd.server_close()
    
    # Stop the thread
    httpd.server_close()
    
    # Wait forever
    httpd.server_close()
    
    # Stop the webserver
    httpd.server_close()
    
    # Wait forever
    httpd.server_close()
    
    # Stop the thread
    httpd.server_close()
    
    # Wait forever
    httpd.server_close()
    
    # Stop the webserver
    httpd.server_close()
    
    # Wait forever
    httpd.server_close()
    
    # Stop the thread
    httpd.server_close()
    
    # Wait forever
    httpd.server_close()
    
    # Stop the webserver
    httpd.server_close()
    
    # Wait forever
    httpd.server_close()
    
    # Stop the thread
    httpd.server_close()
    
    # Wait forever
    httpd.server_close()
    
    # Stop the webserver
    httpd.server_close()
    
    # Wait forever
    httpd.server_close()
    
    # Stop the thread
    httpd.server_close()
    
    # Wait forever
    httpd.server_close()
    
    # Stop the webserver
    httpd.server_close()
    
    # Wait forever
    httpd.server_close()
    
    # Stop the thread
    httpd.server_close()
    
    # Wait forever
    httpd.server_close()
    
    # Stop the webserver
    httpd.server_close()
    
    # Wait forever
    httpd.server_close()
    
    # Stop the thread
    httpd.server_close()
    
    # Wait forever
    httpd.server_close()
    
    # Stop the webserver
    httpd.server_close()
    
    # Wait forever
    httpd.server_close()
    