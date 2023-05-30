#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns fruits or stores a port. """    
    from flask import Flask, render_template, request, jsonify
    app = Flask(__name__)
    
    @app.route('/fruits/')
    def fruits():
        """ Returns all fruits. """
        fruits = ['apple', 'banana', 'cherry']
        return jsonify(fruits)
    
    @app.route('/fruits/<fruit>')
    def fruit(fruit):
        """ Returns one fruit by name. """
        fruits = ['apple', 'banana', 'cherry']
        if fruit in fruits:
            return jsonify(fruit)
        else:
            return 'No such fruit!'
    
    @app.route('/store/port/')
    def store_port():
        """ Stores a port in redis. """
        import redis
        port = int(request.args.get('port'))
        
        client = redis.Redis(host='localhost', port=port, db=0)
        client.sadd('fruits', fruit)
        
        return jsonify(port=port)
    
    app.run(host='0.0.0.0', port=8080)
