#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A endless loop that removes a http request.
    while True:
        try:
            req = requests.get(url)
            req.close()
        except:
            break
    #A endless loop that prints the contents of a file.
    while True:
        try:
            req = requests.get(url)
            req.close()
        except:
            break
        with open('output.txt', 'w') as f:
            f.write(req.text)
            f.close()

