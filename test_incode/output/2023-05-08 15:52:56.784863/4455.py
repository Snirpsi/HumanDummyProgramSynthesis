#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A endless loop that iterates over a http request.
    while True:
        req = requests.get(url)
        soup = BeautifulSoup(req.text, "html.parser")
        
        #Get all links in the page
        allLinks = soup.find_all("a")
        
        #For each link, get its url
        for link in allLinks:
            url = link.get("href")
            
            #Print the url
            print(url)
            
        #Wait for 10 seconds
        time.sleep(10)

