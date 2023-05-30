#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores user input and prints all ports. """    
    ports = []
    
    # Start a server
    server = HTTPServer(('0.0.0.0', 8080), SimpleHTTPRequestHandler)
    
    # Start a thread to listen for connections
    threading.Thread(target=server.serve_forever).start()
    
    # Start a thread to store user input and print all ports
    threading.Thread(target=store_and_print_ports).start()
    
    # Wait until all threads are done
    server.serve_forever()
    
    # Stop the server
    server.socket.close()
    
    # Stop the threads
    server.server_close()
    
    # Stop the thread
    server.join()
    
    # Print the list of ports
    print('\n'.join(ports))
    
