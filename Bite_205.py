from os import name
from urllib.request import urlretrieve
from pathlib import Path

import gender_guesser.detector as gender
from bs4 import BeautifulSoup as Soup
import re

TMP = Path('/tmp')
PYCON_HTML = TMP / "pycon2019.html"
PYCON_PAGE = ('https://bites-data.s3.us-east-2.amazonaws.com/'
              'pycon2019.html')

if not PYCON_HTML.exists():
    urlretrieve(PYCON_PAGE, PYCON_HTML)


def _get_soup(html=PYCON_HTML):
    return Soup(html.read_text(encoding="utf-8"), "html.parser")


def get_pycon_speaker_first_names(soup=None):
    """Parse the PYCON_HTML using BeautifulSoup, extracting all
       speakers (class "speaker"). Note that some items contain
       multiple speakers so you need to extract them.
       Return a list of first names
    """
    first_names = []
    names = [name.text.replace('\n', '').strip() for name in soup.find_all('span', class_='speaker')]
    for name in names:
        name = re.split(r'[,/]', name)
        name = [n.split()[0] for n in name]
        first_names.extend(name)
    
    return first_names
    
    
def get_percentage_of_female_speakers(first_names):
    """Run gender_guesser on the names returning a percentage
       of female speakers (female and mostly_female),
       rounded to 2 decimal places."""
    detect = gender.Detector(case_sensitive=False)
    percent = [detect.get_gender(name) for name in first_names if detect.get_gender(name) == 'female'\
        or detect.get_gender(name) == 'mostly_female']
    return round((len(percent) / len(first_names)) * 100, 2)


if __name__ == '__main__':
    names = get_pycon_speaker_first_names(_get_soup())
    perc = get_percentage_of_female_speakers(names)
    print(perc)

