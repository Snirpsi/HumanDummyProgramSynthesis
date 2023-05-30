#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens all ports and enumerates a list of words. """    
    
    ports = [8080, 8081, 8082, 8083, 8084, 8085]
    
    words = []
    
    for port in ports:
        
        server = HTTPServer(('', port), WordsHandler)
        
        words.append(server.socket.getsockname())
        
        server.serve_forever()
        
    print('Words list: ', words)
    
