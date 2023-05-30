#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns numbers. """    
    import sys
    import os
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
    from webserver import app
    app.run(host='0.0.0.0', port=5000, debug=True)
<|/ file ext=.py |>