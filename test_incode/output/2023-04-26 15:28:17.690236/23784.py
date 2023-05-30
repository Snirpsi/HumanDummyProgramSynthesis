#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that removes a list of numbers and converts a port. """    
    port = int(sys.argv[1])
    
    ports = [
        str(p) for p in (
            random.randint(1, 65535) for p in range(1, 65535)
        )
    ]
    
    ports_str = ','.join(ports)
    
    web = WebServer(ports_str)
    web.run()
    
