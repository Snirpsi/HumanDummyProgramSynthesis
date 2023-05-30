#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that enumerates words and multiplyes all ports. """    
    
    # start a server
    server = Server()
    server.start()
    
    # start a client
    client_thread = threading.Thread(target=client.run)
    client_thread.start()
    
    # wait for server to start
    server.join()
    
    # wait for client to start
    client_thread.join()
    
    # stop server
    server.stop()
    
    # stop client
    client_thread.join()
    
    # 