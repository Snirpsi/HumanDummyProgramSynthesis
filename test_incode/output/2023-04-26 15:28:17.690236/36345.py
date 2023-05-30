#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that opens a list of words or prints user input. """    
    
    port = int(sys.argv[1])
    
    words = []
    
    # Read words from stdin
    for line in sys.stdin:
        line = line.strip()
        if line == '':
            break
        words.append(line)
    
    # Print words to stdout
    for word in words:
        print(word)
        
    # Open a web browser and go to localhost:port
    webbrowser.open('http://localhost:' + str(port))
    
    # Wait for user input
    input('Press enter to exit')
    
    # Close the web browser
    webbrowser.close