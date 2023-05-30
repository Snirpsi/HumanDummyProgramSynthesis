#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates fruits or converts a list of words. """    
    
    from flask import Flask
    from flask import request
    from flask import render_template
    from flask import jsonify
    from flask import Response
    
    app = Flask(__name__)
    
    @app.route('/')
    def index():
        return render_template('index.html')
    
    @app.route('/fruits/')
    def fruits():
        return render_template('fruits.html')
    
    @app.route('/fruits/<word>')
    def fruits_word(word):
        return render_template('fruits_word.html', word=word)
    
    @app.route('/fruits/<word>/<int:num>')
    def fruits_word_num(word, num):
        return render_template('fruits_word_num.html', word=word, num=num)
    
    @app.route('/fruits/<word>/<int:num>/<int:num>')
    def fruits_word_num_num(word, num, num):
        return render_template('fruits_word_num_num.html', word=word, num=num, num=num)
    
    @app.route('/fruits/<word>/<int:num>/<int:num>/<int:num>')
    def fruits_word_num_num_num(word, num, num, num):
        return render_template('fruits_word_num_num_num.html', word=word, num=num, num=num)
    
    @app.route('/fruits/<word>/<int:num>/<int:num>/<int:num>/<int:num>')
    def fruits_word_num_num_num_num(word, num, num, num, num):
        return render_template('fruits_word_num_num_num_num.html', word=word, num=num, num=num, num=num)
    
    @app.route('/fruits/<word>/<int:num>/<int:num>/<int:num>/<int:num>/<int:num>/<int:num>')
    def fruits_word_num_num_num_num_num(word, num, num, num, num, num):
        return render_template('fruits_word_num_num_num_num_num.html', word=word, num=num, num=num, num=num, num=num)
    
    @app.route('/fruits/<word>/<int:num>/<int:num>/<int:num>/<int:num>/<int:num>/<int:num>/<int:num>/<int:num>')
    def fruits_word_num_num_num_num_num_num(word, num, num, num, num, num, num, num):
        return render_template('fruits_word_num_num_num_num_num_num.html', word=word, num=num, num=num, num=num, num=num, num=num)
    
    @app.route('/fruits/<word>/<int:num>/<int:num>/<int:num>/<int:num>/<int:num>/<int:num>/<int:num>/<int:num>/<int:num>/<int:num>/<int:num>')
    def fruits_word_num_num_num_