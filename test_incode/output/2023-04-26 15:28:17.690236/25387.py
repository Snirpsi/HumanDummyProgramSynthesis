#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a list of words and iterates over all ports. """    
    
    words = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    ports = [80, 443]
    
    httpd = HTTPServer(('', 80), WordsHandler)
    httpd.socket = ssl.wrap_socket(httpd.socket, keyfile='key.pem', certfile='cert.pem', server_side=True)
    
    for port in ports:
        httpd.socket = ssl.wrap_socket(httpd.socket, keyfile='key.pem', certfile='cert.pem', server_side=True, server_hostname='localhost', port=port)
    
    httpd.serve_forever()
