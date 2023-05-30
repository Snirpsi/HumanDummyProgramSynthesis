#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints fruits. """    
    
    import os
    import sys
    
    port = 8080
    
    sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
    
    from app import app
    
    app.run(host='0.0.0.0', port=port)
    
