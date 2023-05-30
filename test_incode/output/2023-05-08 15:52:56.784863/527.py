#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A endless loop that enumerates a http request.
    while True:
        #The request is sent to the url and received.
        response = requests.get(url)
        #The response is saved to a file.
        with open('responses.txt', 'w') as f:
            f.write(response.text)
        #The response is saved to a file.
        time.sleep(1)

