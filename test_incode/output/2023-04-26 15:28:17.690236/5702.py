#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that multiplyes a list of words and adds a port. """    
    words = ["hello", "world", "python", "is", "it", "funny"]
    port = "8080"
    
    # Create a socket and bind the port to it.
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(("localhost", int(port)))
    
    # Create a socket and listen for connections.
    sock.listen(1)
    
    # Create a thread to handle connections.
    threads = []
    for sock in threads:
        thread = threading.Thread(target=handle_connection, args=(sock,))
        thread.daemon = True
        thread.start()
    
    # Wait for connections.
    while True:
        connection, client_address = sock.accept()
        
        # Receive the request from the client.
        request = connection.recv(1024)
        
        # Send the response to the client.
        connection.send(str(