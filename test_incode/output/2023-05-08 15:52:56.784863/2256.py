#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A endless loop that removes a http request.
    while True:
        req = requests.get(url)
        if req.status_code == 200:
            print("Removing request from queue")
            req.release()
        else:
            print("Request failed with status code: " + str(req.status_code))
        time.sleep(5)

