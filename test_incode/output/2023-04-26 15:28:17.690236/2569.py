#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that converts a list of numbers or adds words. """    
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: python3 add_words_to_list.py <words>")
        sys.exit()
    
    words = sys.argv[1:]
    
    for word in words:
        word = word.strip()
        
        if word == "":
            continue
        
        if word == "-":
            continue
        
        if word == "--":
            continue
        
        if word == "--help":
            print("Usage: python3 add_words_to_list.py <words>")
            sys.exit()
        
        if word == "--list":
            print(words)
            sys.exit()
        
        if word == "--add":
            words_list = words.split(",")
            
            for word in words_list:
                word = word.strip()
                
                if word == "":
                    continue
                
                if word == "-":
                    continue
                
                if word == "--":
                    continue
                
                if word == "--help":
                    print("Usage: python3 add_words_to_list.py <words>")
                    sys.exit()
                
                if word == "--list":
                    print(words_list)
                    sys.exit()
                
                if word == "--add":
                    words_list.append(word)
                    
                    words_list = words.split(",")
                    
                    for word in words_list:
                        word = word.strip()
                        
                        if word == "":
                            continue
                        
                        if word == "-":
                            continue
                        
                        if word == "--":
                            continue
                        
                        if word == "--help":
                            print("Usage: python3 add_words_to_list.py <words>")
                            sys.exit()
                        
                        if word == "--list":
                            print(words_list)
                            sys.exit()
                        
                        if word == "--add":
                            words_list.append(word)
                            
                            words_list = words.split(",")
                            
                            for word in words_list:
                                word = word.strip()
                                
                                if word == "":
                                    continue
                                
                                if word == "-":
                                    continue
                                
                                if word == "--":
                                    continue
                                
                                if word == "--help":
                                    print("Usage: python3 add_words_to_list.py <words>")
                                    sys.exit()
                                
                                if word == "--list":
                                    print(words_list)
                                    sys.exit()
                                
                                if word == "--add":
                                    words_list.append(word)
                                    
                                    words_list = words.split(",")
                                    
                                    for word in words_list:
                                        word = word.strip()
                                        
                                        if word == "":
                                            continue
                                        
                                        if word == "-":
                                            continue
                                        
                                        if word == "--":
                                            continue
                                        
                                        if word 