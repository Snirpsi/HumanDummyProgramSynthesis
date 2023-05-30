#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a list of numbers. """    
    port = int(sys.argv[1])
    
    numbers = []
    
    # Start a web server
    httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    # Start a thread to serve the request
    threading.Thread(target=httpd.serve_forever).start()
    
    # Wait for the server to start
    httpd.serve_forever()
    
    # Stop the server
    httpd.server_close()
    
    # Print the list of numbers
    for number in numbers:
        print(number)
    
    # Stop the thread
    httpd.shutdown()
    
    # Close the server
    httpd.server_close()
    
    # Stop the server
    httpd.server_close()
    
    # Stop the server
    httpd.server_close()
    
    # Stop the server
    httpd.server_close()
    
    # Stop the server
    httpd.server_close()
    
    # Stop the server
    httpd.server_close()
    
    # Stop the server
    httpd.server_close()
    
    # Stop the server
    httpd.server_close()
    
    # Stop the server
    httpd.server_close()
    
    # Stop the server
    httpd.server_close()
    
    # Stop the server
    httpd.server_close()
    
    # Stop the server
    httpd.server_close()
    
    # Stop the server
    httpd.server_close()
    
    # Stop the server
    httpd.server_close()
    
    # Stop the server
    httpd.server_close()
    
    # Stop the server
    httpd.server_close()
    
    # Stop the server
    httpd.server_close()
    
    # Stop the server
    httpd.server_close()
    
    # Stop the server
    httpd.server_close()
    
    # Stop the server
    httpd.server_close()
    
    # Stop the server
    httpd.server_close()
    
    # Stop the server
    httpd.server_close()
    
    # Stop the server
    httpd.server_close()
    
    # Stop the server
    httpd.server_close()
    
    # Stop the server
    httpd.server_close()
    
    # Stop the server
    httpd.server_close()
    
    # Stop the server
    httpd.server_close()
    
    # Stop the server
    httpd.server_close()
    
    # Stop the server
    httpd.server_close()
    
    # Stop the server
    httpd.server_close()
    
    # Stop the 