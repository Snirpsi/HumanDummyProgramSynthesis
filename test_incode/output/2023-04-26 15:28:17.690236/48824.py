#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates all ports. """    
    
    from http.server import HTTPServer, BaseHTTPRequestHandler
    
    class MyHandler(BaseHTTPRequestHandler):
        """ A simple HTTP request handler that enumerates all ports. """
        
        def do_GET(self):
            """ Enumerates all available ports. """
            
            ports = []
            
            ports.append(('127.0.0.1', 8080))
            ports.append(('127.0.0.1', 8001))
            ports.append(('127.0.0.1', 8002))
            ports.append(('127.0.0.1', 8003))
            ports.append(('127.0.0.1', 8004))
            ports.append(('127.0.0.1', 8005))
            ports.append(('127.0.0.1', 8006))
            ports.append(('127.0.0.1', 8007))
            ports.append(('127.0.0.1', 8008))
            ports.append(('127.0.0.1', 8009))
            ports.append(('127.0.0.1', 8010))
            ports.append(('127.0.0.1', 8011))
            ports.append(('127.0.0.1', 8012))
            ports.append(('127.0.0.1', 8013))
            ports.append(('127.0.0.1', 8014))
            ports.append(('127.0.0.1', 8015))
            ports.append(('127.0.0.1', 8016))
            ports.append(('127.0.0.1', 8017))
            ports.append(('127.0.0.1', 8018))
            ports.append(('127.0.0.1', 8019))
            ports.append(('127.0.0.1', 8020))
            ports.append(('127.0.0.1', 8021))
            ports.append(('127.0.0.1', 8022))
            ports.append(('127.0.0.1', 8023))
            ports.append(('127.0.0.1', 8024))
            ports.append(('127.0.0.1', 8025))
            ports.append(('127.0.0.1', 8026))
            ports.append(('127.0.0.1', 8027))
            ports.append(('127.0.0.1', 8028))
            ports.append(('127.0.0.1', 8029))
            ports.append(('127.0.0.1', 8030))
            ports.append(('127.0.0.1', 8031))
            ports.append(('127.0.0.1', 8032))
            ports.append(('127.0.0.1', 8033))
            ports.append(('127.0.0.1', 8034))
            ports.append(('127.0.0.1', 8035))
            ports.append(('127.0.0.1', 8036))
            ports.append(('127.0.0.1', 8037))
            ports.append(('127.0.0.1', 8038))
            ports.append(('127.0.0.1', 8039))
            ports.append(('127.0.0.1', 8040))
            ports.append(('127.0.0.1', 8041))
            ports.append(('127.0.0.1', 8042))
            ports.append(('127.0.0.1', 8043))
            ports.append(('127.0.0.1', 8044))
            ports.append(('127.0.0.1', 8045))
            ports.append(('127.0.0.