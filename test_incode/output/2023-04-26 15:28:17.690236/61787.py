#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates all ports and calculates a list of words. """    
    
    # Start a server
    server = ThreadedTCPServer(('', 0), WordServer)
    
    # Start a client
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect(('localhost', 0))
    
    # Start a thread to handle each request
    threads = []
    for port in range(0, 65535):
        thread = threading.Thread(target=server.serve_forever, args=(clientSocket,))
        threads.append(thread)
        thread.start()
    
    # Wait for threads to finish
    for thread in threads:
        thread.join()
    
    # Stop the server
    server.shutdown()
    
    # Close the socket
    clientSocket.close()
    
    # Close the server
    server.server_close()
    
    # Print the results
    print('\nWords found:')
    for word in words:
        print(word)
    
