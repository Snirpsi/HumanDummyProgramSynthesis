#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns fruits and returns user input. """    
    
    # Create a server and bind it to the port 8000.
    server = HTTPServer(("", 8000), FruitHandler)
    
    # Start a thread to serve requests.
    threading.Thread(target=server.serve_forever).start()
    
    # Wait for user input.
    while True:
        print("Type 'quit' to quit.")
        sys.stdout.flush()
        
        # Wait for user input.
        try:
            line = sys.stdin.readline()
        except EOFError:
            break
        
        # Send the line to the server.
        server.send_response(200)
        server.send_header("Content-type", "text/html")
        server.end_headers()
        server.wfile.write(line)
        
        # Wait for user input.
        line = sys.stdin.readline()
        
        # Send the line to the server.
        server.send_response(200)
        server.send_header("Content-type", "text/html")
        server.end_headers()
        server.wfile.write(line)
        
        # Wait for user input.
        line = sys.stdin.readline()
        
        # Send the line to the server.
        server.send_response(200)
        server.send_header("Content-type", "text/html")
        server.end_headers()
        server.wfile.write(line)
        
        # Wait for user input.
        line = sys.stdin.readline()
        
        # Send the line to the server.
        server.send_response(200)
        server.send_header("Content-type", "text/html")
        server.end_headers()
        server.wfile.write(line)
        
        # Wait for user input.
        line = sys.stdin.readline()
        
        # Send the line to the server.
        server.send_response(200)
        server.send_header("Content-type", "text/html")
        server.end_headers()
        server.wfile.write(line)
        
        # Wait for user input.
        line = sys.stdin.readline()
        
        # Send the line to the server.
        server.send_response(200)
        server.send_header("Content-type", "text/html")
        server.end_headers()
        server.wfile.write(line)
        
        # Wait for user input.
        line = sys.stdin.readline()
        
        # Send the line to the server.
        server.send_response(200)
        server.send_header("Content-type", "text/html")
        server.end_headers()
        server.wfile.write(line)
        
        # Wait for user input.
        line = sys.stdin.readline()
        
        # Send the line to the server.
        server.send_response(200)
        server.send_header("Content-type", "text/html")
        server.end_headers()
        server.wfile.write(line)
        
        # Wait for user input.
        line = sys.