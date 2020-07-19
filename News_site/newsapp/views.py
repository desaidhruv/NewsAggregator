from django.shortcuts import render
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

# GEtting news from Inshorts

inshorts_r = requests.get("https://inshorts.com/en/read/")
inshorts_soup = BeautifulSoup(inshorts_r.content, 'html.parser')

inshorts_headings = inshorts_soup.find_all('span', attrs={'itemprop': 'headline'})
# toi_head = toi_soup.find_all('span', attrs={'itemprop': 'headline'})

inshorts_headings = inshorts_headings[0:] # removing footers

# toi_head = toi_head[0:-13]
inshorts_news = []

for th in inshorts_headings:
    inshorts_news.append(th.text)

inshorts_headlines = []

# for t in toi_head:
#     toi_headlines.append(t.text)


#Getting news from Times of India

toi_r = requests.get("https://timesofindia.indiatimes.com/briefs")
toi_soup = BeautifulSoup(toi_r.content, 'html.parser')

toi_headings = toi_soup.find_all('div', attrs={'class': 'brief_box'})

toi_headings = toi_headings[0:-50] # removing footers

toi_news = []

for th in toi_headings:
    toi_news.append(th.text)


def index(req):
    return render(req, 'newsapp/index.html', {'inshorts_news':inshorts_news, 'toi_news':toi_news})