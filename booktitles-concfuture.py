from cgitb import html
from matplotlib.pyplot import tick_params
import pandas as pd
import requests
from bs4 import BeautifulSoup
import concurrent.futures
from csv import reader

urls = []
titles = []

with open('bookslinks.csv', 'r') as f:
    file_csv= reader(f)
    for row in file_csv:
        urls.append(row[0])
def transform(url) :
    r = requests.get(str(url))
    soup = BeautifulSoup(r.content,'html.parser')
    title= soup.find('h1').text
    titles.append(title) 
    print(title)
    return

# use concurrent.futures to speed the process
with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(transform,urls)

# with concurrent.futures.ThreadPoolExecutor() as executor:
#     executor.map(transform, urls)

print(len(titles))
df = pd.DataFrame(titles)
df.to_csv('concurrent-titles.csv', index=False)
print('Complete.')
