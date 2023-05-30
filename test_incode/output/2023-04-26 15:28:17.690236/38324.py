#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that iterates over a list of numbers and returns words. """    
    numbers = [int(n) for n in sys.argv[1:]]
    words = [str(n) for n in numbers]
    
    # Write the output to a file
    with open('words.txt', 'w') as outfile:
        for word in words:
            outfile.write(word + '\n')
        
    # Print the output to the screen
    print('\n'.join(words))
    
    # Close the file
    outfile.close()
    
    # Run the server
    httpd.serve_forever()
    
