#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that returns a port. """    
    while True:
        port = random.randint(10000, 30000)
        print('Listening on port {}'.format(port))
        httpd.serve_forever()
