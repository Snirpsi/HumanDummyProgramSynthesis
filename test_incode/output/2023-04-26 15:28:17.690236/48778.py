#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens fruits. """    
    
    from fruits import app
    app.run(host='0.0.0.0', debug=True)

<|/ file ext=.py source=github filename=