#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates all ports and calculates fruits. """    
    
    from flask import Flask
    
    app = Flask(__name__)
    
    @app.route('/')
    def index():
        """ The main page that lists all available ports. """
        
        ports = []
        
        for port in range(1,65535):
            ports.append(port)
            
        return ports
    
    app.run(host='0.0.0.0', port=8080, debug=True)
    
