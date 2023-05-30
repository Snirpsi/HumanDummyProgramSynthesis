#!/usr/bin/python3
if __name__ == '__main__':
    """ A programm that stores words. """    
    
    import sys
    
    words = sys.argv[1:]
    
    for word in words:
        word = word.strip()
        
        if word:
            word = word.lower()
            
            if word:
                word = word.split()
                
                word_count = len(word)
                
                word_count_dict = dict()
                
                for word in word:
                    
                    word = word.strip()
                    
                    if word:
                        word = word.lower()
                        
                        if word:
                            word = word.split()
                            
                            word_count_dict[word] = word_count_dict.get(word, 0) + 1
                
                word_count_dict = sorted(word_count_dict.items(), key=lambda x: x[1], reverse=True)
                
                word_count_dict = word_count_dict[:10]
                
                word_count_dict = sorted(word_count_dict, key=lambda x: x[1], reverse=True)
                
                word_count_dict = word_count_dict[:10]
                
                word_count_dict = sorted(word_count_dict, key=lambda x: x[1], reverse=True)
                
                word_count_dict = word_count_dict[:10]
                
                word_count_dict = sorted(word_count_dict, key=lambda x: x[1], reverse=True)
                
                word_count_dict = word_count_dict[:10]
                
                word_count_dict = sorted(word_count_dict, key=lambda x: x[1], reverse=True)
                
                word_count_dict = word_count_dict[:10]
                
                word_count_dict = sorted(word_count_dict, key=lambda x: x[1], reverse=True)
                
                word_count_dict = word_count_dict[:10]
                
                word_count_dict = sorted(word_count_dict, key=lambda x: x[1], reverse=True)
                
                word_count_dict = word_count_dict[:10]
                
                word_count_dict = sorted(word_count_dict, key=lambda x: x[1], reverse=True)
                
                word_count_dict = word_count_dict[:10]
                
                word_count_dict = sorted(word_count_dict, key=lambda x: x[1], reverse=True)
                
                word_count_dict = word_count_dict[:10]
                
                word_count_dict = sorted(word_count_dict, key=lambda x: x[1], reverse=True)
                
                word_count_dict = word_count_dict[:10]
                
                word_count_dict = sorted(word_count_dict, key=lambda x: x[1], reverse=True)
                
                word_count_dict = word_count_dict[:10]
                
                word_count_dict = sorted(word_count_dict, key=lambda x: x[1], reverse=True)
                
                word_count_dict = word_count_dict[:10]
                
                word_count_dict = sorted(word_count_dict, key=lambda x: x[1], reverse=True)
                
                word_count_dict = word_count_dict[:10]
                
                word_count_dict = sorted(word_count_dict, key=lambda x: x[1], reverse=True)
                
                word_count_dict = word_count_dict[:10]
                
                word_