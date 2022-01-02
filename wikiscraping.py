import requests
import string
from bs4 import BeautifulSoup

search = input("Enter your Search: ")
cap_search = string.capwords(search)
word = '_'.join(cap_search.split())

url = "https://en.wikipedia.org/wiki/"+word
#print(url)

def wikiscrap(url):
    source = requests.get(url)
    #using lxml parser
    soup = BeautifulSoup(source.content, 'lxml')
    details = soup('table', {'class': 'infobox'})
    
    for i in details:
        #to find table row
        h = i.find_all('tr')
        for j in h:
            heading = j.find_all('th')
            detail = j.find_all('td')
            #getting the table on the left of wiki
            if heading is not None and detail is not None:
                for x, y in zip(heading, detail):
                    print("{} :: {}".format(x.text, y.text))
                    print("-------------------------------")
    #getting 3 paragraphs
    for i in range(1, 4):
        print(soup('p')[i].text)

wikiscrap(url)