#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens fruits. """    
    
    server = HTTPServer(("", 80), FruitHandler)
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    
    server.server_close()
    
    print("Server stopped.")

<|/ file filename=fruit