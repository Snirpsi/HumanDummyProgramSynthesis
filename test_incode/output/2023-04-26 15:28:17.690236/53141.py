#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that multiplyes all ports. """    
    ports = [8080, 8081, 8082, 8083, 8084, 8085]
    
    for port in ports:
        httpd = make_server(port, app, host='0.0.0.0', threaded=True)
        print('Serving on port %s' % port)
        httpd.serve_forever()

<|/ file source=github filename=server.py |>