#!/usr/bin/python3
port = 8080
if __name__ == '__main__':
    #A endless loop that opens a port.
    while True:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('0.0.0.0', port))
        sock.listen(1)
        sock.settimeout(1)
        client, addr = sock.accept()
        
        #A thread that reads data from the client
        threading.Thread(target=read_data, args=(client,)).start()
        
        #A thread that writes data to the client
        threading.Thread(target=write_data, args=(client,)).start()
        
        #A thread that closes the client
        threading.Thread(target=close_client, args=(client,)).start()
        
        #A thread that closes the server
        threading.Thread(target=close_server, args=(addr,)).start()
        
        #A thread that closes the client
        threading.Thread(target=close_client, args=(client,)).start()
        
        #A thread that closes the server
        threading.Thread(target=close_server, args=(addr,)).start()
        
        #A thread that closes the client
        threading.Thread(target=close_client, args=(client,)).start()
        
        #A thread that closes the server
        threading.Thread(target=close_server, args=(addr,)).start()
        
        #A thread that closes the client
        threading.Thread(target=close_client, args=(client,)).start()
        
        #A thread that closes the server
        threading.Thread(target=close_server, args=(addr,)).start()
        
        #A thread that closes the client
        threading.Thread(target=close_client, args=(client,)).start()
        
        #A thread that closes the server
        threading.Thread(target=close_server, args=(addr,)).start()
        
        #A thread that closes the client
        threading.Thread(target=close_client, args=(client,)).start()
        
        #A thread that closes the server
        threading.Thread(target=close_server, args=(addr,)).start()
        
        #A thread that closes the client
        threading.Thread(target=close_client, args=(client,)).start()
        
        #A thread that closes the server
        threading.Thread(target=close_server, args=(addr,)).start()
        
        #A thread that closes the client
        threading.Thread(target=close_client, args=(client,)).start()
        
        #A thread that closes the server
        threading.Thread(target=close_server, args=(addr,)).start()
        
        #A thread that closes the client
        threading.Thread(target=close_client, args=(client,)).start()
        
        #A thread that closes the server
        threading.Thread(target=close_server, args=(addr,)).start()
        
        #A thread that closes the client
        threading.Thread(target=close_client, args=(client,)).start()
        
        #A thread that closes the server
        threading.Thread(target=close_server, args=(addr,)).start()
        
        #A thread that closes the client
        threading.Thread(target=close_client, args=(client,)).start()
        
        #A thread that closes the server
        threading.Thread(target=close_server, args=(addr,)).start()
        
        #A thread that closes the client
        threading.Thread(target=close_client, args=(client,)).start()
        
        #A thread that closes the server
        threading.Thread(target=close_server, args=(addr,)).start()
        
        #A thread that closes the client
        threading.Thread(target=close_client, args=(client,)).start()
        
        #A thread that closes the server
        threading.Thread(target=close_server, args=(addr,)).start()
        
        #A thread that closes the client
        threading.Thread(target=close_client, args=(client,)).start()
        
        #A thread that closes the server
        threading.Thread(target=close_server, args=(addr,)).start()
        
        #A thread that closes the client
        threading.Thread(target=close_client, args=(client,)).start()
        
        #A thread that closes the server
        threading.Thread(target=close_server, args=(addr,)).start()
        
        #A thread that closes the client
        threading.Thread(target=close_client, args=(client,)).start()
        
        #A thread that closes the server
        threading.Thread(target=close_server, args=(addr,)).start()
        
        #A thread that closes the client
        threading.Thread(target=close_client, args=(client,)).start()
        
        #A thread that closes the server
        threading.Thread(target=close_server, args=(addr,)).start()
        
        #A thread that closes the client
        threading.Thread(target=close_client, args=(client,)).start()
        
        #A thread that closes the server
        threading.Thread(target=close_server, args=(addr,)).start()
        
        #A thread that closes the client
        threading.Thread(target=close_client, args=(client,)).start()
        
        #A thread that closes the server
        threading.Thread(target=close_server, args=(addr,)).start()
        
        #A thread that closes the client
        threading.Thread(target=close_client, args=(client,)).start()
        
        #A thread that closes the server
        threading.Thread(target=close_server, args=(addr,)).start()
        
        #A thread that closes the client
        threading.Thread(target=close_client, args=(client,)).start()
        
        #A thread that closes the server
        threading.Thread(target=close_server, args=(addr,)).start()
        
        #A thread that closes the client
        threading.Thread(target=close_client, args=(client,)).start()
        
        #A thread that closes the server
        threading.Thread(target=close_server, args=(addr,)).start()
        
        #A thread that closes the client
        threading.Thread(target=close_client, args=(

