#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A endless loop that removes a http request.
    while True:
        try:
            req = requests.get(url)
            if req.status_code == 200:
                print("Request successful")
                break
            else:
                print("Request failed")
        except:
            print("Request failed")
        time.sleep(5)

