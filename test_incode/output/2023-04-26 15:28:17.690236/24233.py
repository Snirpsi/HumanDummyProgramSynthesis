#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that converts user input. """    
    
    import sys
    
    if len(sys.argv) > 1:
        
        filename = sys.argv[1]
        
        with open(filename, 'r') as file:
            
            content = file.read()
            
            content = content.replace('$USER', os.environ['USER'])
            content = content.replace('$HOSTNAME', socket.gethostname())
            
            content = content.replace('$HOSTIP', socket.gethostbyname(socket.gethostname()))
            
            content = content.replace('$HOSTNAME', socket.gethostname())
            
            content = content.replace('$HOSTIP', socket.gethostbyname(socket.gethostname()))
            
            content = content.replace('$HOSTNAME', socket.gethostname())
            
            content = content.replace('$HOSTIP', socket.gethostbyname(socket.gethostname()))
            
            content = content.replace('$HOSTNAME', socket.gethostname())
            
            content = content.replace('$HOSTIP', socket.gethostbyname(socket.gethostname()))
            
            content = content.replace('$HOSTNAME', socket.gethostname())
            
            content = content.replace('$HOSTIP', socket.gethostbyname(socket.gethostname()))
            
            content = content.replace('$HOSTNAME', socket.gethostname())
            
            content = content.replace('$HOSTIP', socket.gethostbyname(socket.gethostname()))
            
            content = content.replace('$HOSTNAME', socket.gethostname())
            
            content = content.replace('$HOSTIP', socket.gethostbyname(socket.gethostname()))
            
            content = content.replace('$HOSTNAME', socket.gethostname())
            
            content = content.replace('$HOSTIP', socket.gethostbyname(socket.gethostname()))
            
            content = content.replace('$HOSTNAME', socket.gethostname())
            
            content = content.replace('$HOSTIP', socket.gethostbyname(socket.gethostname()))
            
            content = content.replace('$HOSTNAME', socket.gethostname())
            
            content = content.replace('$HOSTIP', socket.gethostbyname(socket.gethostname()))
            
            content = content.replace('$HOSTNAME', socket.gethostname())
            
            content = content.replace('$HOSTIP', socket.gethostbyname(socket.gethostname()))
            
            content = content.replace('$HOSTNAME', socket.gethostname())
            
            content = content.replace('$HOSTIP', socket.ge