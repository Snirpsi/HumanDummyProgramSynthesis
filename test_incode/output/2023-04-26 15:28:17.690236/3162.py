#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates fruits. """    
    from flask import Flask, render_template, request
    app = Flask(__name__)
    app.debug = True
    app.secret_key = 'super secret key'
    
    @app.route('/')
    def index():
        return render_template('index.html')
    
    @app.route('/fruits/')
    def fruits():
        return render_template('fruits.html')
    
    @app.route('/fruits/<fruit>')
    def fruit(fruit):
        return render_template('fruit.html', fruit=fruit)
    
    app.run(host='0.0.0.0', port=5000)
