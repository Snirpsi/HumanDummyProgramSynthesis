#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates fruits. """    
    
    import os
    import sys
    
    sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
    
    from webserver import app
    
    app.run(host="0.0.0.0", port=8080, debug=True)
    
