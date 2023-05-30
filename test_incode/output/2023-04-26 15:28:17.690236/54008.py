#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns fruits. """    
    from flask import Flask, render_template
    app = Flask(__name__)
    app.run(host='0.0.0.0')
    
@app.route('/fruits')
def fruits():
    """ Return a list of fruits. """
    return render_template('fruits.html')
    
if __name__ == '__main__':
