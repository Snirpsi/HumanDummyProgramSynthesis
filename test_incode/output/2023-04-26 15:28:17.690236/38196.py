#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a list of words. """    
    
    words = []
    
    # Open the file containing the words to serve
    with open('words.txt') as words_file:
        words = words_file.read().splitlines()
    
    # Serve the words in the file as a JSON response
    json_response = json.dumps(words)
    
    # Send the response back to the client
    print(json_response)
    
    # Close the file
    words_file.close()
    
    # Close the HTTP connection
    connection.close()
    
    # Return the response
    return json_response
    
