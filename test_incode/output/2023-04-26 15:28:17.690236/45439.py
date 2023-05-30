#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores words. """    
    
    words = []
    
    # Handle GET request
    if request.method == 'GET':
        
        # Read all words from the file
        with open('words.txt', 'r') as file:
            words = file.read().splitlines()
            
        # Display all words to the user
        for word in words:
            print(word)
            
    # Handle POST request
    elif request.method == 'POST':
        
        # Read the POST data
        post_data = request.get_data()
        
        # Split the POST data into words
        words = post_data.split()
        
        # Display all words to the user
        for word in words:
            print(word)
            
    # Handle all other requests
    else:
        print('Invalid request')
        
    # Close the file
    file.close()
    
    # Return the response
    return render_template('index.html')
    
