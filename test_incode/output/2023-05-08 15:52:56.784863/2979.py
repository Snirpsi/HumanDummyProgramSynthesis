#!/usr/bin/python3
words = ["hello","world","!"]
if __name__ == '__main__':
    #A endless loop that calculates words.
    while True:
        words = words + ["!"]
        print(words)
        time.sleep(1)

