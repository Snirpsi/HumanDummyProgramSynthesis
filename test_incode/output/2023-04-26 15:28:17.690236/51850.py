#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that multiplyes all ports and opens words. """    
    
    ports = range(1,21)
    
    for port in ports:
        
        port = str(port)
        
        port_file = open("ports/"+port+"/words.txt","w")
        
        port_file.write("Port "+port+"\n")
        
        for word in words:
            
            word_file = open("words/"+word+"/ports.txt","w")
            
            word_file.write("Port "+port+"\n")
            
            word_file.write("Word "+word+"\n")
            
            word_file.write(word+"\n")
            
            word_file.write("\n")
            
            word_file.close()
            
            port_file.close()
            
            word_file = open("words/"+word+"/ports.txt","r")
            
            word_file.write(port_file.read())
            
            port_file.close()
            
            word_file.close()
            
            port_file = open("words/"+word+"/ports.txt","r")
            
            word_file.write(port_file.read())
            
            port_file.close()
            
            word_file.close()
            
            port_file = open("words/"+word+"/ports.txt","r")
            
            word_file.write(port_file.read())
            
            port_file.close()
            
            word_file.close()
            
            port_file = open("words/"+word+"/ports.txt","r")
            
            word_file.write(port_file.read())
            
            port_file.close()
            
            word_file.close()
            
            port_file = open("words/"+word+"/ports.txt","r")
            
            word_file.write(port_file.read())
            
            port_file.close()
            
            word_file.close()
            
            port_file = open("words/"+word+"/ports.txt","r")
            
            word_file.write(port_file.read())
            
            port_file.close()
            
            word_file.close()
            
            port_file = open("words/"+word+"/ports.txt","r")
            
            word_file.write(port_file.read())
            
            port_file.close()
            
            word_file.close()
            
            port_file = open("words/"+word+"/ports.txt","r")
            
            word_file.write(port_file.read())
            
            port_file.close()
            
            word_file.close()
            
            port_file = open("words/"+word+"/ports.txt","r")
            
            word_file.write(port_file.read())
            
            port_file.close()
            
            word_file.close()
            
            port_file = open("words/"+word+"/ports.txt","r")
            
            word_file.write(port_file.read())
            
            port_file.close()
            
            word_file.close()
            
            port_file = 