# import library
import requests
from bs4 import  BeautifulSoup
import get_list_diseases

data = []
for get_data in get_list_diseases.get_content_per_page():
    data.append(get_data)

for query in data:
    query = query.replace(' ', '+')
    url = 'https://www.google.com/search?q={}&oq={}&aqs=chrome..69i57.5180025j0j1&sourceid=chrome&ie=UTF-8'.format(query, query) #url
    print(url)
    print()
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}#headers
    source=requests.get(url, headers=headers).text # url source
    soup = BeautifulSoup(source, 'html.parser')
    search_div = soup.find_all(class_='PZPZlf') # find all divs tha contains search result
    for result in search_div: # loop result list
        f = open("result_2.txt", "a")
        f.write("\n")
        f.write(result.text)
        f.write("\n")
        f.close()
    #print('Title: %s'%result.h3.string) #geting h3 
    #print('Url: %s'%result.a.get('href')) #geting a.href 
    #print('Description: %s'%result.find(class_='st').text)