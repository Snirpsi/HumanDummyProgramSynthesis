#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts fruits. """    
    
    from flask import Flask, render_template, request, jsonify
    app = Flask(__name__, static_url_path='')
    
    @app.route('/fruits/')
    def fruits():
        return render_template('fruits.html')
    
    @app.route('/fruits/<fruit>')
    def fruit(fruit):
        return render_template('fruit.html')
    
    @app.route('/fruits/<fruit>/<int:num>')
    def fruit(fruit, num):
        return render_template('fruit.