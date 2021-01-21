from collections import namedtuple

from bs4 import BeautifulSoup
import requests

# feed = https://news.python.sc/, to get predictable results we cached
# first two pages - use these:
# https://bites-data.s3.us-east-2.amazonaws.com/news.python.sc/index.html
# https://bites-data.s3.us-east-2.amazonaws.com/news.python.sc/index2.html

Entry = namedtuple('Entry', 'title points comments')


def _create_soup_obj(url):
    """Need utf-8 to properly parse emojis"""
    resp = requests.get(url)
    resp.encoding = "utf-8"
    return BeautifulSoup(resp.text, "html.parser")


def get_top_titles(url, top=5):
    """Parse the titles (class 'title') using the soup object.
       Return a list of top (default = 5) titles ordered descending
       by number of points and comments.
    """
    soup = _create_soup_obj(url)
    top_titles = []
    titles = soup.findAll(class_='title')
    points_and_comments = soup.findAll('span', class_='smaller')
    points_and_comments = [p.text.split() for p in points_and_comments if len(p.text.split()) > 1]
    
    for i in range(len(points_and_comments)):
        point = points_and_comments[i]
        points = int(point[0])
        comments = int(point[-2])
        title = titles[i].text.replace('\n', '')
        title_info = Entry(title=title, points=points, comments=comments)
        top_titles.append(title_info)
    
    top_titles = sorted(top_titles, key=lambda x: x.points + x.comments, reverse=True)
    return [top_titles[i] for i in range(top)]






url1 = 'https://bites-data.s3.us-east-2.amazonaws.com/news.python.sc/index.html'
url2 = 'https://bites-data.s3.us-east-2.amazonaws.com/new/python.sc/index2.html'
print(get_top_titles(url1))
