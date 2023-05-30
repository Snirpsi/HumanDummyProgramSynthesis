#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that returns a port. """    
    port = 8080
    print("Starting server on port " + str(port))
    httpd = make_server('', port, app)
    httpd.serve_forever()
