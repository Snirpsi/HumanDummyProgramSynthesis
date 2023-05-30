#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a list of numbers and adds a list of numbers. """    
    
    import os
    import sys
    
    sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
    
    from webserver import app
    
    port = int(os.environ.get("PORT", 5000))
    
    app.run(host='0.0.0.0', port=port)
    
