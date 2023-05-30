#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates a port. """    
    import sys
    import socketserver
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--port', type=int, help='port to enumerate')
    args = parser.parse_args()
    port = args.port
    
    httpd = socketserver.TCPServer(("", port), MyHandler)
    print("serving at port", port)
    httpd.serve_forever()

<|/ file source=github |>