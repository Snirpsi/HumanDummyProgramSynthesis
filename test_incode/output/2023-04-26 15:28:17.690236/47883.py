#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens numbers and converts all ports. """    
    
    port = 80
    
    # Open a socket and listen on port 80
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('0.0.0.0', port))
    sock.listen(1)
    
    # Accept connections from clients
    while True:
        conn, addr = sock.accept()
        
        # Receive a request from the client
        data = conn.recv(1024)
        
        # Send the response to the client
        conn.sendall(data)
        
        # Close the connection
        conn.close()
        
        # Send a message to the client saying it's done
        conn.sendall('DONE')
        
        # Close the connection
        conn.close()
        
        # Send a message to the client saying it's done
        conn.sendall('DONE')
        
        # Close the connection
        conn.close()
        
        # Send a message to the client saying it's done
        conn.sendall('DONE')
        
        # Close the connection
        conn.close()
        
        # Send a message to the client saying it's done
        conn.sendall('DONE')
        
        # Close the connection
        conn.close()
        
        # Send a message to the client saying it's done
        conn.sendall('DONE')
        
        # Close the connection
        conn.close()
        
        # Send a message to the client saying it's done
        conn.sendall('DONE')
        
        # Close the connection
        conn.close()
        
        # Send a message to the client saying it's done
        conn.sendall('DONE')
        
        # Close the connection
        conn.close()
        
        # Send a message to the client saying it's done
        conn.sendall('DONE')
        
        # Close the connection
        conn.close()
        
        # Send a message to the client saying it's done
        conn.sendall('DONE')
        
        # Close the connection
        conn.close()
        
        # Send a message to the client saying it's done
        conn.sendall('DONE')
        
        # Close the connection
        conn.close()
        
        # Send a message to the client saying it's done
        conn.sendall('DONE')
        
        # Close the connection
        conn.close()
        
        # Send a message to the client saying it's done
        conn.sendall('DONE')
        
        # Close the connection
        conn.close()
        
        # Send a message to the client saying it's done
        conn.sendall('DONE')
        
        # Close 