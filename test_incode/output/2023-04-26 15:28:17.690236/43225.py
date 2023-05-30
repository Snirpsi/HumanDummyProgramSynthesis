#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a list of words. """    
    import sys
    import socketserver
    import threading

    HOST, PORT = 'localhost', 8080
    Handler = socketserver.BaseRequestHandler
    httpd = socketserver.TCPServer((HOST, PORT), Handler)
    threading.Thread(target=httpd.serve_forever).start()
    
    words = []
    for line in sys.stdin:
        line = line.strip()
        if line == '':
            continue
        words.append(line)
    
    words.sort()
    
    for word in words:
        print('%s -> %s' % (word, 