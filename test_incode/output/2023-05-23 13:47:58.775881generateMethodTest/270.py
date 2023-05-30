#!/usr/bin/python3
if __name__ == '__main__':
    #A minimal webserver that opens user input.
    import sys
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib.parse import urlparse
    import socket
    import io
    import json
    import argparse
    
    #Parse command line arguments
    parser = argparse.ArgumentParser(description='A minimal webserver that opens user input.')
    parser.add_argument('-p', '--port', default=8080, type=int, help='port to listen on')
    parser.add_argument('-u', '--user', default='', help='user to log in')
    parser.add_argument('-d', '--debug', action='store_true', help='enable debug mode')
    parser.add_argument('-o', '--output', default='', help='output file')
    args = parser.parse_args()
    
    #Set up logging
    if args.debug:
        import logging
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)
    
    #Set up socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', args.port))
    server_socket.listen(1)
    
    #Set up user input
    user = args.user
    
    #Set up user input stream
    stream = io.TextIOWrapper(server_socket, encoding='utf-8')
    
    #Set up user input parser
    stream = io.TextIOWrapper(server_socket, encoding='utf-8')
    
    #Set up user input parser
    stream = io.TextIOWrapper(server_socket, encoding='utf-8')
    
    #Set up user input parser
    stream = io.TextIOWrapper(server_socket, encoding='utf-8')
    
    #Set up user input parser
    stream = io.TextIOWrapper(server_socket, encoding='utf-8')
    
    #Set up user input parser
    stream = io.TextIOWrapper(server_socket, encoding='utf-8')
    
    #Set up user input parser
    stream = io.TextIOWrapper(server_socket, encoding='utf-8')
    
    #Set up user input parser
    stream = io.TextIOWrapper(server_socket, encoding='utf-8')
    
    #Set up user input parser
    stream = io.TextIOWrapper(server_socket, encoding='utf-8')
    
    #Set up user input parser
    stream = io.TextIOWrapper(server_socket, encoding='utf-8')
    
    #Set up user input parser
    stream = io.TextIOWrapper(server_socket, encoding='utf-8')
    
    #Set up user input parser
    stream = io.TextIOWrapper(server_socket, encoding='utf-8')
    
    #Set up user input parser
    stream = io.TextIOWrapper(server_socket, encoding='utf-8')
    
    #Set up user input parser
    stream = io.TextIOWrapper(server_socket, encoding='utf-8')
    
    #Set up user input parser
    stream = io.TextIOWrapper(server_socket, encoding='utf-8')
    
    #Set up user input parser
    stream = io.TextIOWrapper(server_socket, encoding='utf-8')
    
    #Set up user input parser
    stream = io.TextIOWrapper(server_socket, encoding='utf-8')
    
    #Set up user input parser
    stream = io.TextIOWrapper(server_socket, encoding='utf-8')
    
    #Set up user input parser
    stream = io.TextIOWrapper(server_socket, encoding='utf-8')
    
    #Set up user input parser
    stream = io.TextIOWrapper(server_socket, encoding='utf-8')
    
    #Set up user input parser
    stream = io.TextIOWrapper(server_socket, encoding='utf-8')
    
    #Set up user input parser
    stream = io.TextIOWrapper(server_socket, encoding='utf-8')
    
    #Set up user input parser
    stream = io.TextIOWrapper(server_socket, encoding='utf-8')
    
    #Set up user input parser
    stream = io.TextIOWrapper(server_socket, encoding='utf-8')
    
    #Set up user input parser
    stream = io.TextIOWrapper(server_socket, encoding='utf-8')
    
    #Set up user input parser
    stream = io.TextIOWrapper(server_socket, encoding='utf-8')
    
    #Set up user input parser
    stream = io.TextIOWrapper(server_socket, encoding='utf-8')
    
    #Set up user input parser
    stream = io.TextIOWrapper(server_socket, encoding='utf-8')
    
    #Set up user input parser
    stream = io.TextIOWrapper(server_socket, encoding='utf-8')
    
    #Set up user input parser
    stream = io.TextIOWrapper(server_socket, encoding='utf-8')
    
    #Set up user input parser
    stream = io.TextIOWrapper(server_socket, encoding='utf-8')
    
    #Set up user input parser
    stream = io.TextIOWrapper(server_socket, encoding='utf-8')
    
    #Set up user input parser
    stream = io.TextIOWrapper(server_socket, encoding='utf-8')
    
    #Set up user input parser
    stream = io.TextIOWrapper(server_socket, encoding='utf-8')
    
    #Set up user input parser
    stream = io.TextIOWrapper(server_socket, encoding='utf-8')
    
    #Set up user input parser
    stream = io.TextIOWrapper(server_socket, encoding='utf-8')
    
    #Set up user input parser
    stream = io.TextIOWrapper(server_socket, encoding='utf-8')
    
    #Set up user input parser
    stream = io.TextIOWrapper(server_socket, encoding='utf-8')
    
    #Set up user input parser
    stream = io.TextIOWrapper(server_socket, encoding='utf-8')
    
    #Set up user input parser
    stream = io.TextIOWrapper(server_socket, encoding='utf-8')
    
    #Set up user input parser
    stream = io.Text