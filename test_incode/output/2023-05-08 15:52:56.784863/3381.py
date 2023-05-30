#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A endless loop that calculates a http request.
    while True:
        try:
            req = requests.get(url)
            if req.status_code == 200:
                print("Got a 200 OK response")
                break
            else:
                print("Got a {} response".format(req.status_code))
        except requests.exceptions.RequestException as e:
            print("Got a {} response".format(e))
            time.sleep(5)

