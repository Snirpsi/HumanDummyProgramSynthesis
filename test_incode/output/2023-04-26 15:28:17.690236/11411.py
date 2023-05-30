#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts user input or iterates over user input. """    
    
    import sys
    
    if len(sys.argv) > 1:
        
        # Read input from stdin
        stdin = sys.stdin.read()
        
        # Convert input to JSON
        json_input = json.loads(stdin)
        
        # Print JSON
        print(json.dumps(json_input))
        
    else:
        
        # Iterate over user input
        for input in sys.stdin:
            
            # Convert input to JSON
            json_input = json.loads(input)
            
            # Print JSON
            print(json.dumps(json_input))
            
