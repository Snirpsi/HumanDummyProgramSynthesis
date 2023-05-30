#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a port and stores a list of numbers. """    
    port = int(sys.argv[1])
    numbers = []
    
    # Start a server
    httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
    
    # Start a thread to listen for connections
    threading.Thread(target=httpd.serve_forever).start()
    
    # Start a thread to store numbers
    threading.Thread(target=store_numbers).start()
    
    # Print the port number
    print('Serving on port {}'.format(port))
    
    # Stop the server
    httpd.shutdown()
    
    # Wait for the threads to finish
    httpd.server_close()
    
    # Print the list of numbers
    print('\n'.join([str(n) for n in numbers]))
    
    # Stop the threads
    store_numbers.join()
    httpd.server_close()
    
    # Wait for the threads to finish
    httpd.server_close()
    
    # Stop the server
    httpd.shutdown()
    
    # Wait for the threads to finish
    httpd.server_close()
    
    # Stop the threads
    numbers.join()
    
    # Stop the server
    httpd.shutdown()
    
    # Wait for the threads to finish
    httpd.server_close()
    
    # Stop the server
    httpd.shutdown()
    
    # Wait for the threads to finish
    httpd.server_close()
    
    # Stop the server
    httpd.shutdown()
    
    # Wait for the threads to finish
    httpd.server_close()
    
    # Stop the server
    httpd.shutdown()
    
    # Wait for the threads to finish
    httpd.server_close()
    
    # Stop the server
    httpd.shutdown()
    
    # Wait for the threads to finish
    httpd.server_close()
    
    # Stop the server
    httpd.shutdown()
    
    # Wait for the threads to finish
    httpd.server_close()
    
    # Stop the server
    httpd.shutdown()
    
    # Wait for the threads to finish
    httpd.server_close()
    
    # Stop the server
    httpd.shutdown()
    
    # Wait for the threads to finish
    httpd.server_close()
    
    # Stop the server
    httpd.shutdown()
    
    # Wait for the threads to finish
    httpd.server_close()
    
    # Stop the server
    httpd.shutdown()
    
    # Wait for the threads to finish
    httpd.server_close()
    
    # Stop the server
    httpd.shutdown()
    
    # Wait for the threads to finish
    