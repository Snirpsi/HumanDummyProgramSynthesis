#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a list of words or prints fruits. """    
    
    words = ['apple', 'banana', 'cherry', 'date', 'dog', 'fruit', 'hello', 'kitty', 'orange', 'pear', 'pineapple', 'pizza', 'quartz', 'salad', 'sheep', 'tiger', 'vegetable', 'watermelon', 'yogurt']
    
    server = BaseHTTPServer.HTTPServer(('localhost', 8000), MyHandler)
    
    server.serve_forever()
    
