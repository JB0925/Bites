import os
import re
from difflib import SequenceMatcher
import itertools
from urllib.request import urlretrieve
import requests
import os

# prep
TAG_HTML = re.compile(r'<category>([^<]+)</category>')
TEMPFILE = os.path.join('/tmp', 'feed')
MIN_TAG_LEN = 10
IDENTICAL = 1.0
SIMILAR = 0.95

# urlretrieve(
#     'https://bites-data.s3.us-east-2.amazonaws.com/tags.xml',
#     TEMPFILE
# )

url = 'https://bites-data.s3.us-east-2.amazonaws.com/tags.xml'
response = requests.get(url).text

if not os.path.exists('Bites/bite23.txt'):
    with open('bite23.txt', 'w', encoding='utf-8') as f:
        f.write(response)

def _get_tags(tempfile='bite23.txt'):
    """Helper to parse all tags from a static copy of PyBites' feed,
       providing this here so you can focus on difflib"""
    with open(tempfile) as f:
        content = f.read().lower()
    # take a small subset to keep it performant
    tags = TAG_HTML.findall(content)
    tags = [tag for tag in tags if len(tag) > MIN_TAG_LEN]
    return set(tags)


def get_similarities(tags=None):
    """Should return a list of similar tag pairs (tuples)"""
    tags = tags or list(_get_tags())
    similar_tags = []
    
    for tag in tags:
        for i in range(len(tags)-1):
            match = SequenceMatcher(None, tag, tags[i]).ratio()
            if match >= SIMILAR and tag != tags[i]:
                words = (tag, tags[i])
                similar_tags.append(words)

    return similar_tags
    


print(get_similarities())