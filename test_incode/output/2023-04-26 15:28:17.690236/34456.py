#!/usr/bin/python3
if __name__ == '__main__':
    """ A function that returns fruits and opens all ports. """    
    
    ports = openPorts()
    
    for port in ports:
        
        fruits = openFruits(port)
        
        for fruit in fruits:
            
            fruits[fruit] = fruits[fruit].replace("\n", "")
            
            fruits[fruit] = fruits[fruit].replace("\r", "")
            
            fruits[fruit] = fruits[fruit].replace("\t", "")
            
            fruits[fruit] = fruits[fruit].replace(",", "")
            
            fruits[fruit] = fruits[fruit].replace("?", "")
            
            fruits[fruit] = fruits[fruit].replace("!", "")
            
            fruits[fruit] = fruits[fruit].replace("(", "")
            
            fruits[fruit] = fruits[fruit].replace(")", "")
            
            fruits[fruit] = fruits[fruit].replace(",", "")
            
            fruits[fruit] = fruits[fruit].replace(";", "")
            
            fruits[fruit] = fruits[fruit].replace("'", "")
            
            fruits[fruit] = fruits[fruit].replace("<", "")
            
            fruits[fruit] = fruits[fruit].replace(">", "")
            
            fruits[fruit] = fruits[fruit].replace("&", "")
            
            fruits[fruit] = fruits[fruit].replace("'", "")
            
            fruits[fruit] = fruits[fruit].replace("(", "")
            
            fruits[fruit] = fruits[fruit].replace(")", "")
            
            fruits[fruit] = fruits[fruit].replace(",", "")
            
            fruits[fruit] = fruits[fruit].replace(";", "")
            
            fruits[fruit] = fruits[fruit].replace("'", "")
            
            fruits[fruit] = fruits[fruit].replace("<", "")
            
            fruits[fruit] = fruits[fruit].replace(">", "")
            
            fruits[fruit] = fruits[fruit].replace("&", "")
            
            fruits[fruit] = fruits[fruit].replace("'", "")
            
            fruits[fruit] = fruits[fruit].replace("(", "")
            
            fruits[fruit] = fruits[fruit].replace(")", "")
            
            fruits[fruit] = fruits[fruit].replace(",", "")
            
            fruits[fruit] = fruits[fruit].replace(";", "")
            
            fruits[fruit] = fruits[fruit].replace("'", "")
            
            fruits[fruit] = fruits[fruit].replace("(", "")
            
            fruits[fruit] = fruits[fruit].replace(")", "")
            
            fruits[