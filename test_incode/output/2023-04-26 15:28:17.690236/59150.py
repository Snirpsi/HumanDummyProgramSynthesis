#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a port. """    
    import sys
    port = int(sys.argv[1])
    
    from geventwebsocket.handler import WebSocketHandler
    from geventwebsocket.server import WebSocketServer
    
    server = WebSocketServer(("", port), WebSocketHandler)
    server.serve_forever()

<|/ file source=github |>