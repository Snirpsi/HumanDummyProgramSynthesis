#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes words. """    
    
    import os
    import socketserver
    import webbrowser
    
    HOST, PORT = 'localhost', 8080
    
    server = socketserver.TCPServer((HOST, PORT), webbrowser.