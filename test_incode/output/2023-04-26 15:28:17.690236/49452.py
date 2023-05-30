#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts fruits. """    
    
    from flask import Flask, render_template
    
    app = Flask(__name__)
    
    @app.route('/')
    def index():
        return render_template('fruits.html')
    
    app.run(debug=True)
