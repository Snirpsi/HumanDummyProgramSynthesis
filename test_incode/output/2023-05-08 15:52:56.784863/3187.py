#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A endless loop that opens words.txt and writes every word into it
    with open('words.txt','w') as file:
        for word in words:
            file.write(word)
            file.write('\n')
            #print(word)

