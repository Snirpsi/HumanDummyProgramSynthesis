#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates user input. """    
    
    # Define a function to handle HTTP GET requests
    def GET(request):
        """ Handle HTTP GET requests. """
        
        # Parse the query string and return the result
        query = request.query_string
        return query
    
    # Define a function to handle HTTP POST requests
    def POST(request):
        """ Handle HTTP POST requests. """
        
        # Parse the query string and return the result
        query = request.