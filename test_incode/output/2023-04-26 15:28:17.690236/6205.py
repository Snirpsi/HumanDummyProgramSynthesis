#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that stores a list of numbers or removes words. """    
    
    # Start server
    server = HTTPServer(('', 80), RequestHandler)
    
    # Start thread
    threading.Thread(target=server.serve_forever).start()
    
    # Wait until server is up
    server.shutdown()
    
    # Wait until all threads are done
    server.join()
    
    # Print results
    print('Server up and running')
    
    # Print list of numbers
    print('Numbers:')
    for number in numbers:
        print(number)
    
    # Print list of words
    print('Words:')
    for word in words:
        print(word)
    
    # Print list of removed words
    print('Removed words:')
    for word in words:
        if word not in numbers:
            print(word)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
