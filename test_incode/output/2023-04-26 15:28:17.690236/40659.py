#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that returns all ports. """    
    ports = []
    
    ports.append( ('0.0.0.0', 80) )
    ports.append( ('127.0.0.1', 80) )
    
    for port in ports:
        print('Starting port {} on {}'.format(port[0], port[1]))
        
        try:
            httpd = HTTPServer(port, WSGIHandler())
            httpd.serve_forever()
        except KeyboardInterrupt:
            print('\nExiting...')
            
