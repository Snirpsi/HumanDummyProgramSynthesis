#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that adds words. """    
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: %s <words>" % sys.argv[0])
        sys.exit()
    
    words = sys.argv[1:]
    
    for word in words:
        word = word.strip()
        
        if word == '':
            continue
        
        word = word.lower()
        
        if word not in word_list:
            word_list.append(word)
            
    print("\n".join(word_list))
    
