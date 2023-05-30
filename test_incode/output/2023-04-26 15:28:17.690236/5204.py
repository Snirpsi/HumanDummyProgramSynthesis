#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that prints a list of words and adds words. """    
    words = ['word1', 'word2', 'word3']
    
    # Create a web server
    httpd = HTTPServer(('localhost', 8000), WordsHandler)
    
    # Start it
    httpd.serve_forever()
    
    # Stop it
    httpd.server_close()
    
    # 