import requests
import webbrowser
from bs4 import BeautifulSoup
#user_input=input("Ask the Question:")

#prt=print("Trying to Get the articles")

google_search= requests.get("https://www.who.int/emergencies/diseases/en/")

soup = BeautifulSoup(google_search.text, features='html')

search_results = soup.select('.module a')

#[x.extract() for x in soup.find_all('script')]
#[x.extract() for x in soup.find_all('style')]
#[x.extract() for x in soup.find_all('meta')]
#[x.extract() for x in soup.find_all('noscript')]


'''html =soup.contents
for i in html:
    print(i)'''


'''html = soup.prettify("utf-8")
with open("output1.html", "wb") as file:
    file.write(html)

'''
'''i=1
for link in search_results: 
    print(link.get('href'))
    with open("output1.html", "wb") as file:
    file.write(html)
'''

for link in search_results: 
    if link!= '<a href="/csr/disease/zika/en/">':
        print(link.get('href'))
    else:
        break