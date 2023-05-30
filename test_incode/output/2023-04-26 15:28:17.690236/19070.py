#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a port and removes a port. """    
    port = 8080
    
    # Create a socket and bind it to the specified port
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', port))
    
    # Listen for incoming connections
    sock.listen(10)
    
    # Create a thread to handle each connection
    thr = threading.Thread(target=handle_connection, args=(sock,))
    
    # Start the thread
    thr.start()
    
    # Wait until the thread is done
    thr.join()
    
    # Close the socket
    sock.close()
    
    # Stop the thread
    thr.stop()
    
    # Close the server
    server.