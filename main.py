# import library
import requests
from bs4 import  BeautifulSoup

def get_content_per_page():
    string_url = "https://idnmedis.com/daftar-penyakit-a-z"
    for page in range(2, 28):
        print()
        print("-----------------")
        print(string_url)
        print("-----------------")
        URL = string_url
        get_url = requests.get(URL)
        content_page = BeautifulSoup(get_url.content, 'html.parser')
        job_elements = content_page.find_all("a", class_="aalmanual")
        string_url = "https://idnmedis.com/daftar-penyakit-a-z/" + str(page)
        if len(job_elements) == 0:
            print("tidak ada nama penyakit") 
        for element in job_elements:
            print(element.text)
    return job_elements

get_content_per_page()