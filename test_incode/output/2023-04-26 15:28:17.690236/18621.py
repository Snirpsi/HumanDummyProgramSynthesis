#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts words. """    
    from flask import Flask, render_template, request
    from words import Words
    app = Flask(__name__)
    app.config['DEBUG'] = True
    app.config['SECRET_KEY'] = 'secret!'
    
    @app.route('/')
    def index():
        """ Main page. """
        return render_template('index.html')
    
    @app.route('/words')
    def words():
        """ Main page. """
        return render_template('words.html')
    
    @app.route('/words/<word>')
    def word(word):
        """ Main page. """
        return render_template('word.html', word=word)
    
    app.run(host='0.0.0.0', port=5000)
    
