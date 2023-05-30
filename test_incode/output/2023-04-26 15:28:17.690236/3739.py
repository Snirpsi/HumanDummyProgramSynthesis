#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints fruits. """    
    
    import os
    import socketserver
    import cgi
    import random
    
    HOST, PORT = 'localhost', 8080
    
    server = socketserver.TCPServer((HOST, PORT), cgi.FieldStorage