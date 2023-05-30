#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens words or converts a list of numbers. """    
    port = int(sys.argv[1])
    
    # Open the port and listen for incoming connections
    httpd = HTTPServer(("", port), WordsHandler)
    httpd.serve_forever()
    
    # Convert a list of numbers to words
    words = []
    for i in range(int(sys.argv[2])):
        words.append(str(i))
    
    # Print the words to the user
    print("Words: ", end="")
    for word in words:
        print(word, end="")
    print("")
    
