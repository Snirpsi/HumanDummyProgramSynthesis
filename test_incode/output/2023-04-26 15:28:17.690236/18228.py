#!/usr/bin/python3
if __name__ == '__main__':
    """ A endless loop that iterates over all ports and iterates over a list of words. """    
    ports = range(1,65535)
    words = ['word1','word2','word3','word4','word5','word6','word7','word8','word9','word10','word11','word12','word13','word14','word15','word16','word17','word18','word19','word20','word21','word22','word23','word24','word25','word26','word27','word28','word29','word30','word31','word32','word33','word34','word35','word36','word37','word38','word39','word40','word41','word42','word43','word44','word45','word46','word47','word48','word49','word50','word51','word52','word53','word54','word55','word56','word57','word58','word59','word60','word61','word62','word63','word64','word65','word66','word67','word68','word69','word70','word71','word72','word73','word74','word75','word76','word77','word78','word79','word80','word81','word82','word83','word84','word85','word86','word87','word88','word89','word90','word91','word92','word93','word94','word95','word96','word97','word98','word99','word100']
    
    while True:
        for port in ports:
            
            # Create a socket and bind it to the port
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.bind(("", port))
            
            # Listen for incoming connections
            sock.listen(1)
            
            # Accept connection
            client, address = sock.accept()
            
            # Receive the message and print it
            print("Connected by", address)
            message = client.recv(1024)
            
            # Send the message back to the client
            client.send(message)
            
            # Close the socket
            client.close()
            
            # Break the loop if no more connections are left
            if sock