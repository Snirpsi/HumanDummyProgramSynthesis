#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a list of words or removes a port. """    
    
    words = ['word1', 'word2', 'word3', 'word4', 'word5']
    
    port = 5000
    
    server = SimpleHTTPRequestHandler
    
    httpd = socketserver.TCPServer(('', port), server)
    
    httpd.serve_forever()
    
