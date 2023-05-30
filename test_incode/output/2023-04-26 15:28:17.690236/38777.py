#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates fruits. """    
    
    # Start a webserver
    server = HTTPServer(('localhost', 8080), FruitCalculator)
    
    # Start a thread to handle requests
    threading.Thread(target=server.serve_forever).start()
    
    # Wait until CTRL+C is pressed
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        server.shutdown()
        
    # Close the server
    server.server_close()
    
    # Stop the thread
    server.shutdown()
    
    # Close the server
    server.server_close()
    
    # Stop the server
    server.shutdown()
    
    # Close the server
    server.server_close()
    
    # Stop the server
    server.shutdown()
    
    # Close the server
    server.server_close()
    
    # Stop the server
    server.shutdown()
    
    # Close the server
    server.server_close()
    
    # Stop the server
    server.shutdown()
    
    # Close the server
    server.server_close()
    
    # Stop the server
    server.shutdown()
    
    # Close the server
    server.server_close()
    
    # Stop the server
    server.shutdown()
    
    # Close the server
    server.server_close()
    
    # Stop the server
    server.shutdown()
    
    # Close the server
    server.server_close()
    
    # Stop the server
    server.shutdown()
    
    # Close the server
    server.server_close()
    
    # Stop the server
    server.shutdown()
    
    # Close the server
    server.server_close()
    
    # Stop the server
    server.shutdown()
    
    # Close the server
    server.server_close()
    
    # Stop the server
    server.shutdown()
    
    # Close the server
    server.server_close()
    
    # Stop the server
    server.shutdown()
    
    # Close the server
    server.server_close()
    
    # Stop the server
    server.shutdown()
    
    # Close the server
    server.server_close()
    
    # Stop the server
    server.shutdown()
    
    # Close the server
    server.server_close()
    
    # Stop the server
    server.shutdown()
    
    # Close the server
    server.server_close()
    
    # Stop the server
    server.shutdown()
    
    # Close the server
    server.server_close()
    
    # Stop the server
    server.shutdown()
    
    # Close the server
    