#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over all ports. """    
    
    ports = []
    
    # Open a socket to listen on all available ports
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind socket to local host and port
    sock.bind(('', 0))
    
    # Listen for incoming connections
    sock.listen(10)
    
    # Start server
    ports.append(sock)
    
    # Start web server
    web_server = HTTPServer(("", 0), SimpleHTTPRequestHandler)
    
    # Start threads
    threading.Thread(target=web_server.serve_forever).start()
    threading.Thread(target=web_server.serve_forever).start()
    
    # Wait until all threads are done
    web_server.server_close()
    
    # Wait until all servers are done
    for port in ports:
        port.join()
    
    # Close socket
    sock.close()
    
    # Print server status
    print("Server running at http://127.0.0.1:%d/" % port)
    
