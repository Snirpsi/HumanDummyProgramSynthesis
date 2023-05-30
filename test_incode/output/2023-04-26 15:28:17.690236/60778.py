#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates numbers. """    
    
    import os
    import sys
    
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
    
    from server import app
    app.run(host='0.0.0.0', port=5000)
    
