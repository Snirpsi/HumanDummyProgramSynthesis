#!/usr/bin/python3
numbers = [1,2,3,4,9]
if __name__ == '__main__':
    #A minimal webserver that adds a list of numbers.
    import sys
    sys.path.append('./')
    from webserver import app
    app.run(host='0.0.0.0', port=8000, debug=True)

