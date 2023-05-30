#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A endless loop that iterates over a http request.
    while True:
        req = requests.get(url)
        if req.status_code == 200:
            soup = BeautifulSoup(req.text, "html.parser")
            links = soup.find_all("a")
            for link in links:
                print(link.get("href"))
        else:
            print("Something went wrong")
        time.sleep(1)

