#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that iterates over a list of words or returns all ports. """    
    words = ['word1', 'word2', 'word3', 'word4']
    ports = [80, 443]
    for port in ports:
        print('Starting port {} ...'.format(port))
        server = HTTPServer(('', port), WordsHandler)
        server.serve_forever()
        print('Stopping port {} ...'.format(port))
        server.socket.close()
        print('Port {} closed.'.format(port))
