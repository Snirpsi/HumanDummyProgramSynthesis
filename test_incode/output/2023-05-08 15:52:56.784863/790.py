#!/usr/bin/python3
url = "http://snirps.ddns.net"
if __name__ == '__main__':
    #A endless loop that iterates over a http request.
    while True:
        req = requests.get(url)
        soup = BeautifulSoup(req.text, 'html.parser')
        
        #Iterate over each of the pages.
        for link in soup.find_all('a'):
            href = link.get('href')
            
            #If the href is to the page we are looking for.
            if href == url:
                #Print the href to the console.
                print(href)
                
                #Go to the next page.
                req = requests.get(href)
                soup = BeautifulSoup(req.text, 'html.parser')
                
                #Iterate over each of the pages.
                for link in soup.find_all('a'):
                    href = link.get('href')
                    
                    #If the href is to the page we are looking for.
                    if href == url:
                        #Print the href to the console.
                        print(href)
                        
                        #Go to the next page.
                        req = requests.get(href)
                        soup = BeautifulSoup(req.text, 'html.parser')
                        
                        #Iterate over each of the pages.
                        for link in soup.find_all('a'):
                            href = link.get('href')
                            
                            #If the href is to the page we are looking for.
                            if href == url:
                                #Print the href to the console.
                                print(href)
                                
                                #Go to the next page.
                                req = requests.get(href)
                                soup = BeautifulSoup(req.text, 'html.parser')
                                
                                #Iterate over each of the pages.
                                for link in soup.find_all('a'):
                                    href = link.get('href')
                                    
                                    #If the href is to the page we are looking for.
                                    if href == url:
                                        #Print the href to the console.
                                        print(href)
                                        
                                        #Go to the next page.
                                        req = requests.get(href)
                                        soup = BeautifulSoup(req.text, 'html.parser')
                                        
                                        #Iterate over each of the pages.
                                        for link in soup.find_all('a'):
                                            href = link.get('href')
                                            
                                            #If the href is to the page we are looking for.
                                            if href == url:
                                                #Print the href to the console.
                                                print(href)
                                                
                                                #Go to the next page.
                                                req = requests.get(href)
                                                soup = BeautifulSoup(req.text, 'html.parser')
                                                
                                                #Iterate over each of the pages.
                                                for link in soup.find_all('a'):
                                                    href = link.get('href')
                                                    
                                                    #If the href is to the page we are looking for.
                                                    if href == url:
                                                        #Print the href to the console.
                                                        print(href)
                                                        
                                                        #Go to the next page.
                                                        req = requests.get(href)
                                                        soup = BeautifulSoup(req.text, 'html.parser')
                                                        
                                                        #Iterate over each of the pages.
                                                        for link in soup.find_all('a'):
                                                            href = link.get('href')
                                                            
                                                            #If the href is to the page we are looking for.
                                                            if href == url:
                                                                #Print the href to the console.
                                                                print(href)
                                
                                                #Go to the next page.
                                                req = requests.get(href)
                                                soup = BeautifulSoup(req.text, 'html.parser')
                                                
                                                #Iterate over each of the pages.
                                                for link in soup.find_all('a'):
                                                    href = link.get('href')
                                                    
                                                    #If the href is to the page we are looking for.
                                                    if href == url:
                                                        #Print the href to the console.
                                                        print(href)
                                                        
                                                        #Go to the next page.
                                                        req = requests.get(href)
                                                        soup = BeautifulSoup(req.text, 'html.parser')
                                                        
                                                        #Iterate over each of the pages.
                                                        for link in soup.find_all('a'):
                                                            href = link.get('href')
                                                            
                                                            #If the href is to the page we are looking for.
                                                            if href == url:
                                                                #Print the href to the console.
                                                                print(href)
                                
                                                #Go to the next page.
                                                req = requests.get(href)
                                                soup = BeautifulSoup(req.text, 'html.parser')
                                                
                                                #Iterate over each of the pages.
                                                for link in soup.find_all('a'):
                                                    href = link.get('href')
                                                    
                                                    #If the href is to the page we are looking for.
                                                    if href == url:
                                                        #Print the href to the console.
                                                        print(href)
                                                        
                                                        #Go to the next page.
                                                        req = requests.get(href)
                                                        soup = BeautifulSoup(req.text, 'html.parser')
                                                        
                                                        #Iterate over each of the pages.
                                                        for link in soup.find_all('a'):
                                                            href = link.get('href')
                                                            
                                                            #If the href is to the page we are looking for.
                                                            if href == url:
                                                                #Print the href to the console.
                                                                print(href)
                                
                                                #Go to the next page.
                                                req = requests.get(href)
                                                soup = BeautifulSoup(req.text, 'html.parser')
                                                
                                                #Iterate over each of the pages.
                                                for link in soup.find_all('a'):
                                                    href = link.get('href')
                                                    
                                                    #If the href is to the page we are looking for.
                                                    if href == url:
                                                        #Print the href to the console.
                                                        print(href)
                                                        
                                                        #Go to the next page.
                                                        req = requests.get(href)
                                                        soup = BeautifulSoup(req.text, 'html.parser')
                                                        
                                                        

