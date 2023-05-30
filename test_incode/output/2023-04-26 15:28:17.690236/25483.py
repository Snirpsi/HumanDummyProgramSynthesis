#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes all ports and stores a list of numbers. """    
    ports = []
    
    # Create a server and listen on all available ports
    server = HTTPServer(("", 0), Handler)
    
    # Start a thread to handle incoming connections
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.daemon = True
    server_thread.start()
    
    # Wait for connections
    port = input("Enter a port to listen on: ")
    ports.append(port)
    
    # Close the server
    server.shutdown()
    
    # Wait for thread to finish
    server_thread.join()
    
    # Print the list of ports
    print("Ports: {}".format(ports))
    
    # Close the server
    server.server_close()
    
    # Close the thread
    server_thread