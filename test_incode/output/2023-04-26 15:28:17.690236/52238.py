#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores all ports and prints words. """    
    ports = [8080, 8081, 8082, 8083, 8084, 8085]
    words = ["hello", "world", "python", "flask", "flask", "flask", "flask"]
    
    for port in ports:
        server = HTTPServer(('', port), WordsHandler)
        server.serve_forever()
    
