#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a port and stores words. """    
    port = int(sys.argv[1])
    words = []
    
    # Print the port number
    print('Starting web server on port ' + str(port))
    
    # Start a thread to serve the words from the port and store them
    threading.Thread(target=serve_words).start()
    
    # Wait for server to start serving words and store them in words
    time.sleep(5)
    
    # Print the words and exit
    print('Words:')
    for word in words:
        print(word)
    
    # Stop the server
    server.shutdown()
    
    # Wait for server to exit
    time.sleep(5)
    
    # Stop the thread
    thread.join()
    
    # Stop the server
    server.socket.close()
    
    # Stop the thread
    thread.join()
    
    # Print the port number
    print('Exiting')
    
    # Stop the server
    server.shutdown()
    
    # Wait for server to exit
    time.sleep(5)
    
    # Stop the thread
    thread.join()
    
    # Print the port number
    print('Exiting')
    
    # Stop the server
    server.shutdown()
    
    # Wait for server to exit
    time.sleep(5)
    
    # Stop the thread
    thread.join()
    
    # Print the port number
    print('Exiting')
    
    # Stop the server
    server.shutdown()
    
    # Wait for server to exit
    time.sleep(5)
    
    # Stop the thread
    thread.join()
    
    # Print the port number
    print('Exiting')
    
    # Stop the server
    server.shutdown()
    
    # Wait for server to exit
    time.sleep(5)
    
    # Stop the thread
    thread.join()
    
    # Print the port number
    print('Exiting')
    
    # Stop the server
    server.shutdown()
    
    # Wait for server to exit
    time.sleep(5)
    
    # Stop the thread
    thread.join()
    
    # Print the port number
    print('Exiting')
    
    # Stop the server
    server.shutdown()
    
    # Wait for server to exit
    time.sleep(5)
    
    # Stop the thread
    thread.join()
    
    # Print the port number
    print('Exiting')
    
    # Stop the server
    server.shutdown()
    
    # Wait for server to exit
    time.sleep(5)
    
    # Stop the thread
    thread.join()
    
    # Print the port number
    print('Exiting')
    