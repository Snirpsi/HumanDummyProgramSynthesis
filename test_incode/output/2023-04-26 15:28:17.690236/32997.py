#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens fruits and multiplyes all ports. """    
    
    # Open the ports
    ports = [8080, 8081, 8082]
    
    # Open the server
    server = HTTPServer(("", 0), FruitServer)
    
    # Start listening on all ports
    server.serve_forever()
    
    # Close the server
    server.socket.close()

<|/ file filename=fruitserver.py source=github |>