#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over all ports. """    
    
    ports = [int(p) for p in sys.argv[1:]]
    
    while True:
        for port in ports:
            print("Starting port {}".format(port))
            
            server = ThreadedTCPServer(("", port), ThreadedTCPHandler)
            server.serve_forever()
            
        print("Stopping all ports")
        
        server.shutdown()
        
        print("Stopping server")
        
        server.server_close()
        
        print("Stopping thread")
        
        server.join()
        
        print("All ports stopped")
        
