#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that enumerates words and adds all ports. """    
    
    wordlist = Wordlist("wordlist.txt")
    
    ports = []
    
    ports.append(WordlistPort("wordlist.txt"))
    
    ports.append(WordlistPort("wordlist.txt", wordlist))
    
    ports.append(WordlistPort("wordlist.txt", wordlist, wordlist))
    
    ports.append(WordlistPort("wordlist.txt", wordlist, wordlist, wordlist))
    
    ports.append(WordlistPort("wordlist.txt", wordlist, wordlist, wordlist, wordlist))
    
    ports.append(WordlistPort("wordlist.txt", wordlist, wordlist, wordlist, wordlist, wordlist))
    
    ports.append(WordlistPort("wordlist.txt", wordlist, wordlist, wordlist, wordlist, wordlist, wordlist))
    
    ports.append(WordlistPort("wordlist.txt", wordlist, wordlist, wordlist, wordlist, wordlist, wordlist, wordlist))
    
    ports.append(WordlistPort("wordlist.txt", wordlist, wordlist, wordlist, wordlist, wordlist, wordlist, wordlist, wordlist))
    
    ports.append(WordlistPort("wordlist.txt", wordlist, wordlist, wordlist, wordlist, wordlist, wordlist, wordlist, wordlist))
    
    ports.append(WordlistPort("wordlist.txt", wordlist, wordlist, wordlist, wordlist, wordlist, wordlist, wordlist, wordlist))
    
    ports.append(WordlistPort("wordlist.txt", wordlist, wordlist, wordlist, wordlist, wordlist, wordlist, wordlist, wordlist, wordlist))
    
    ports.append(WordlistPort("wordlist.txt", wordlist, wordlist, wordlist, wordlist, wordlist, wordlist, wordlist, wordlist, wordlist))
    
    ports.append(WordlistPort("wordlist.txt", wordlist, wordlist, wordlist, wordlist, wordlist, wordlist, wordlist, wordlist, wordlist))
    
    ports.append(WordlistPort("wordlist.txt", wordlist, wordlist, wordlist, wordlist, wordlist, wordlist, wordlist, wordlist, wordlist, wordlist))
    
    ports.append(WordlistPort("wordlist.txt", wordlist, wordlist, wordlist, wordlist, wordlist, wordlist, wordlist, wordlist, wordlist, wordlist))
    
    ports.append(WordlistPort("wordlist.txt", wordlist, wordlist, wordlist, wordlist, wordlist, wordlist, wordlist, wordlist, wordlist))
    
    ports.append(WordlistPort("wordlist.txt", wordlist, wordlist, wordlist, wordlist, wordlist, wordlist, wordlist, wordlist, wordlist))
    
    ports.append(Word