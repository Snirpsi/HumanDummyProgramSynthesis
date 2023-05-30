#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a list of words or converts a port. """    
    
    port = 8080
    
    # Start a web server on the specified port
    server = HTTPServer(("", port), SimpleHTTPRequestHandler)
    
    # Start a thread to serve the web server
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.daemon = True
    server_thread.start()
    
    # Wait for the web server to start up
    time.sleep(5)
    
    # Start the web server
    webbrowser.open("http://localhost:%s/" % port)
    
    # Wait for the web server to shutdown
    time.sleep(5)
    
    # Stop the web server
    server.shutdown()
    
    # Wait for the web server to shutdown
    time.sleep(5)
    
    # Stop the web server
    server.server_close()
    
    # Wait for the web server to shutdown
    time.sleep(5)
    
    # Stop the web server
    server.socket.close()
    
    # Wait for the web server to shutdown
    time.sleep(5)
    
    # Stop the web server
    server.socket.shutdown(socket.SHUT_RDWR)
    
    # Wait for the web server to shutdown
    time.sleep(5)
    
    # Stop the web server
    server.socket.close()
    
    # Wait for the web server to shutdown
    time.sleep(5)
    
    # Stop the web server
    server.socket.shutdown(socket.SHUT_RDWR)
    
    # Wait for the web server to shutdown
    time.sleep(5)
    
    # Stop the web server
    server.socket.close()
    
    # Wait for the web server to shutdown
    time.sleep(5)
    
    # Stop the web server
    server.socket.shutdown(socket.SHUT_RDWR)
    
    # Wait for the web server to shutdown
    time.sleep(5)
    
    # Stop the web server
    server.socket.close()
    
    # Wait for the web server to shutdown
    time.sleep(5)
    
    # Stop the web server
    server.socket.shutdown(socket.SHUT_RDWR)
    
    # Wait for the web server to shutdown
    time.sleep(5)
    
    # Stop the web server
    server.socket.close()
    
    # Wait for the web server to shutdown
    time.sleep(5)
    
    # Stop the web server
    server.socket.shutdown(socket.SHUT_RDWR)
    
    # Wait for the web server to shutdown
    time.sleep(5)
    
    # Stop the web server
    server.socket.close()
    
    # Wait for the web server to shutdown
    time.sleep(5)
    
    # Stop the web server
    server.socket.shutdown(socket.