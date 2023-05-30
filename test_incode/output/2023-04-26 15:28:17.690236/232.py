#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a port and multiplyes a port. """    
    import socketserver
    
    HOST, PORT = "localhost", 9999
    
    server = socketserver.TCPServer((HOST, PORT), SimpleHTTPRequestHandler)
    
    print("serving at port", PORT)
    server.serve_forever()
    
