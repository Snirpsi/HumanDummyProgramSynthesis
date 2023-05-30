#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that calculates all ports and adds a list of words. """    
    ports = []
    
    # start a webserver
    httpd = HTTPServer(('', 80), Handler)
    
    # start a thread that listens for requests
    threading.Thread(target=httpd.serve_forever).start()
    
    # start a thread that adds words to the ports list
    threading.Thread(target=add_words).start()
    
    # wait for the threads to finish
    httpd.serve_forever()
    
    # print out the list of ports
    print('\n'.join(ports))
    
    # stop the threads
    httpd.shutdown()
    
    # close the server
    httpd.server_close()
    
    # close the threads
    httpd.join()
    
    # print out the list of ports
    print('\n'.join(ports))
    
    # stop the threads
    httpd.shutdown()
    
    # close the server
    httpd.server_close()
    
    # close the threads
    httpd.join()
    
    # print out the list of ports
    print('\n'.join(ports))
    
    # stop the threads
    httpd.shutdown()
    
    # close the server
    httpd.server_close()
    
    # close the threads
    httpd.join()
    
    # print out the list of ports
    print('\n'.join(ports))
    
    # stop the threads
    httpd.shutdown()
    
    # close the server
    httpd.server_close()
    
    # close the threads
    httpd.join()
    
    # print out the list of ports
    print('\n'.join(ports))
    
    # stop the threads
    httpd.shutdown()
    
    # close the server
    httpd.server_close()
    
    # close the threads
    httpd.join()
    
    # print out the list of ports
    print('\n'.join(ports))
    
    # stop the threads
    httpd.shutdown()
    
    # close the server
    httpd.server_close()
    
    # close the threads
    httpd.join()
    
    # print out the list of ports
    print('\n'.join(ports))
    
    # stop the threads
    httpd.shutdown()
    
    # close the server
    httpd.server_close()
    
    # close the threads
    httpd.join()
    
    # print out the list of ports
    print('\n'.join(ports))
    
    # stop the threads
    httpd.shutdown()
    
    # close the server
    httpd.server_close()
    
    # close the threads
    httpd.join()
    
    # print out the list of ports
    print('\n'.join(