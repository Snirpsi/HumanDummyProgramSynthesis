#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a list of words or opens a port. """    
    
    port = int(sys.argv[1])
    
    words = []
    
    # Open a port and listen for connections
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', port))
    sock.listen(1)
    
    # Start a thread that iterates over the list of words and prints them
    threading.Thread(target=print_words).start()
    
    # Start a thread that opens a connection and prints it
    threading.Thread(target=print_connection).start()
    
    # Wait for the server to terminate
    sock.close()
    
    # Wait for the threads to terminate
    thread1.join()
    thread2.join()
    
    # Print the results
    print("\n".join([w for w in words if w]))
    
    # Close the socket
    sock.close()
    
