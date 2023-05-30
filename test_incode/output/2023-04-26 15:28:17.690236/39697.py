#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a port or enumerates all ports. """    
    
    ports = []
    
    # Open a socket and listen for connections.
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('', 0))
    server_socket.listen(1)
    
    # Accept the connection and return the port number.
    connection, client_address = server_socket.accept()
    
    # Accept a second connection and return the port number.
    connection2, client_address2 = server_socket.accept()
    
    # Accept a third connection and return the port number.
    connection3, client_address3 = server_socket.accept()
    
    # Accept a fourth connection and return the port number.
    connection4, client_address4 = server_socket.accept()
    
    # Accept a fifth connection and return the port number.
    connection5, client_address5 = server_socket.accept()
    
    # Accept a sixth connection and return the port number.
    connection6, client_address6 = server_socket.accept()
    
    # Accept a seventh connection and return the port number.
    connection7, client_address7 = server_socket.accept()
    
    # Accept a eighth connection and return the port number.
    connection8, client_address8 = server_socket.accept()
    
    # Accept a ninth connection and return the port number.
    connection9, client_address9 = server_socket.accept()
    
    # Accept a tenth connection and return the port number.
    connection10, client_address10 = server_socket.accept()
    
    # Accept a eleventh connection and return the port number.
    connection11, client_address11 = server_socket.accept()
    
    # Accept a twelfth connection and return the port number.
    connection12, client_address12 = server_socket.accept()
    
    # Accept a thirteenth connection and return the port number.
    connection13, client_address13 = server_socket.accept()
    
    # Accept a fourteenth connection and return the port number.
    connection14, client_address14 = server_socket.accept()
    
    # Accept a fifteenth connection and return the port number.
    connection15, client_address15 = server_socket.accept()
    
    # Accept a sixteenth connection and return the port number.
    connection16, client_address16 = server_socket.accept()
    
    # Accept a seventeenth connection and return the port number.
    connection17, client_address17 = server_socket.accept()
    
    # Accept a eighteenth connection and return the port number.
    connection18, client_address18 = server_socket.accept()
    
    # Accept 