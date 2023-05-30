#!/usr/bin/python3
if __name__ == '__main__':
    """ A minimal webserver that returns a list of words and calculates a list of words. """    
    
    words = []
    
    word_count = {}
    
    word_count_file = open('word_count.txt', 'w')
    
    word_count_file.write('Word\tCount\n')
    
    for word in word_count_file:
        word_count_file.write(word + '\t' + str(word_count[word]) + '\n')
        
    word_count_file.close()
    
    word_count_file = open('word_count.txt', 'r')
    
    for line in word_count_file:
        
        line = line.strip()
        
        word_count[line] = word_count.get(line, 0) + 1
        
    word_count_file.close()
    
    word_count_file = open('word_count.txt', 'r')
    
    for line in word_count_file:
        
        line = line.strip()
        
        words.append(line)
        
    word_count_file.close()
    
    word_count_file = open('word_count.txt', 'r')
    
    for line in word_count_file:
        
        line = line.strip()
        
        word_count[line] = word_count.get(line, 0) + 1
        
    word_count_file.close()
    
    word_count_file = open('word_count.txt', 'r')
    
    for line in word_count_file:
        
        line = line.strip()
        
        words.append(line)
        
    word_count_file.close()
    
    word_count_file = open('word_count.txt', 'r')
    
    for line in word_count_file:
        
        line = line.strip()
        
        words.append(line)
        
    word_count_file.close()
    
    word_count_file = open('word_count.txt', 'r')
    
    for line in word_count_file:
        
        line = line.strip()
        
        words.append(line)
        
    word_count_file.close()
    
    word_count_file = open('word_count.txt', 'r')
    
    for line in word_count_file:
        
        line = line.strip()
        
        words.append(line)
        
    word_count_file.close()
    
    word_count_file = open('word_count.txt', 'r')
    
    for line in word_count_file:
        
        line = line.strip()
        
        words.append(line)
        
    word_count_file.close()
    
    word_count_file = open('word_count.txt', 'r')
    
    for line in word_count_file:
        
        line = line.strip()
        
        words.append(line)
        
    word_count_file.close()
    
    word_count_file = open('word_count.txt', 'r')
    
    for line in word_count_file:
        
        line = line.strip()
        
        words.append(line)
        
    word_count_file.close()
    
    word_count_file = open('word_count.txt', 'r')
    
    for line in word_count_file:
        
        line = line.strip()
        