#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that returns a port. """    
    port = int(sys.argv[1])
    
    # start a server on the given port
    server = Server()
    server.serve(port)
    
    # wait for the server to finish its work
    server.join()
    
    # close the server
    server.close()
    
    # return the port number
    return port
