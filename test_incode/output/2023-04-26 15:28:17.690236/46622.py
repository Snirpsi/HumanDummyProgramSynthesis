#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns all ports or calculates a list of numbers. """    
    
    ports = []
    
    # Open a socket and listen for connections
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 0))
    server_socket.listen(1)
    
    # Accept connection and then start a thread to handle it
    while True:
        conn, addr = server_socket.accept()
        
        # Start a thread to handle connection
        thread = threading.Thread(target=handle_connection, args=(conn, addr))
        thread.start()
        
        # Accept connection and then start a thread to handle it
        thread = threading.Thread(target=handle_connection, args=(conn, addr))
        thread.start()
        
        # Accept connection and then start a thread to handle it
        thread = threading.Thread(target=handle_connection, args=(conn, addr))
        thread.start()
        
        # Accept connection and then start a thread to handle it
        thread = threading.Thread(target=handle_connection, args=(conn, addr))
        thread.start()
        
        # Accept connection and then start a thread to handle it
        thread = threading.Thread(target=handle_connection, args=(conn, addr))
        thread.start()
        
        # Accept connection and then start a thread to handle it
        thread = threading.Thread(target=handle_connection, args=(conn, addr))
        thread.start()
        
        # Accept connection and then start a thread to handle it
        thread = threading.Thread(target=handle_connection, args=(conn, addr))
        thread.start()
        
        # Accept connection and then start a thread to handle it
        thread = threading.Thread(target=handle_connection, args=(conn, addr))
        thread.start()
        
        # Accept connection and then start a thread to handle it
        thread = threading.Thread(target=handle_connection, args=(conn, addr))
        thread.start()
        
        # Accept connection and then start a thread to handle it
        thread = threading.Thread(target=handle_connection, args=(conn, addr))
        thread.start()
        
        # Accept connection and then start a thread to handle it
        thread = threading.Thread(target=handle_connection, args=(conn, addr))
        thread.start()
        
        # Accept connection and then start a thread to handle it
        thread = threading.Thread(target=handle_connection, args=(conn, addr))
        thread.start()
        
        # Accept connection and then start a thread to handle it
        thread = threading.Thread(target=handle_connection, args=(conn, addr))
        thread.start()
        
        # Accept connection and then start a thread to handle it
        thread = threading.Thread(target=handle_connection, args=(conn, addr))
        thread.start()
        
        # Accept connection and then start a thread to handle it
        thread = threading.Thread(target=handle_connection, args=(conn, addr))
        