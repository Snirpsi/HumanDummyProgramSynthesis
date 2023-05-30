#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens user input. """    
    from webserver import app
    app.run(host='0.0.0.0', port=5000, debug=True)

<|/ file source=github filename=webserver.py |>