from cgitb import html
from matplotlib.pyplot import tick_params
import pandas as pd
import requests
from bs4 import BeautifulSoup
import concurrent.futures
from csv import reader
import urllib.request

urls = []
titles = []

with open('bookslinks.csv', 'r') as f:
    file_csv= reader(f)
    for row in file_csv:
        urls.append(row[0])
# def transform(url) :
#     r = requests.get(str(url))
#     soup = BeautifulSoup(r.content,'html.parser')
#     title= soup.find('h1').text
#     titles.append(title) 
#     print(title)
    # return
def load_url(url, timeout):
    resp=urllib.request.urlopen(url, timeout=timeout).read()
    req = urllib.request.Request(url=url)
    html = resp.read().decode()
    soup = BeautifulSoup(html,'html')
    return (soup,req,resp) 
    
# use concurrent.futures to speed the process
with concurrent.futures.ThreadPoolExecutor() as executor:
    future_to_url=dict((executor.submit(load_url, ulr,60), ulr) for ulr in urls)
    
    for future in concurrent.futures.as_completed(future_to_url):
            url= future_to_url[future]
            try:
                print('%r page is %d bytes' % (
                          url, len(future.result())))
            except Exception as e:
                print('%r generated an exception: %s' % (
                          url, e))
print(len(titles))
df = pd.DataFrame(titles)
df.to_csv('concurrent-titles_as_completed.csv', index=False)
print('Complete.')