#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints numbers or enumerates a list of numbers. """    
    
    port = 8080
    
    try:
        server = HTTPServer(("", port), MyHandler)
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.socket.close()
        print("Server shut down")

<|/ file filename=server.py ext=.py |>