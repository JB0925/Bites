from collections import namedtuple, Counter
import re
from typing import NamedTuple

import feedparser

SPECIAL_GUEST = 'Special guest'

# using _ as min/max are builtins
Duration = namedtuple('Duration', 'avg max_ min_')

# static copy, original: https://pythonbytes.fm/episodes/rss
URL = 'https://bites-data.s3.us-east-2.amazonaws.com/python_bytes'
IGNORE_DOMAINS = {'https://pythonbytes.fm', 'http://pythonbytes.fm',
                  'https://twitter.com', 'https://training.talkpython.fm',
                  'https://talkpython.fm', 'http://testandcode.com'}


class PythonBytes:

    def __init__(self, url=URL):
        """Load the feed url into self.entries using the feedparser module."""
        self.entries = []
        all_entries = feedparser.parse(URL)
        all_entries = [entry for entry in all_entries['entries']]
        
        for item in all_entries:
            item = {k:v for k, v in item.items() if k != 'summary'}
            self.entries.append(item)



    def get_episode_numbers_for_mentioned_domain(self, domain: str) -> list:
        """Return a list of episode IDs (itunes_episode attribute) of the
           episodes the pass in domain was mentioned in.
        """
        return [item['itunes_episode'] for item in self.entries if domain in str(item)]
                
        

    def get_most_mentioned_domain_names(self, n: int = 15) -> list:
        """Get the most mentioned domain domains. We match a domain using
           regex: "https?://[^/]+" - make sure you only count a domain once per
           episode and ignore domains in IGNORE_DOMAINS.
           Return a list of (domain, count) tuples (use Counter).
        """
        all_domains = []

        for item in self.entries:
            domains = re.findall(r'https?://[^/]+', str(item))
            domains = list(set(item for item in domains if item not in IGNORE_DOMAINS and\
                'amazonaws' not in item and 'itunes.com' not in item))
            all_domains.extend(domains)
        
        return Counter(all_domains).most_common(n)


    def number_episodes_with_special_guest(self) -> int:
        """Return the number of episodes that had one of more special guests
           featured (use SPECIAL_GUEST).
        """
        count = 0
        
        for item in self.entries:
            if SPECIAL_GUEST in str(item):
                count += 1
        
        return count

    def get_average_duration_episode_in_seconds(self) -> NamedTuple:
        """Return the average duration in seconds of a Python Bytes episode, as
           well as the shortest and longest episode in hh:mm:ss notation.
           Return the results using the Duration namedtuple.
        """
        average_duration = sorted([item['itunes_duration'] for item in self.entries])
        most, least = average_duration[-2], min(average_duration)
        total_seconds = 0

        for time in average_duration:
            hours, minutes, seconds = time.split(':')
            total_seconds += int(minutes) * 60 + int(seconds)
        
        average = int(total_seconds / len(average_duration))
        return Duration(avg=average, max_=most, min_=least)


p = PythonBytes()
# print(p.get_episode_numbers_for_mentioned_domain('realpython.com'))
# print(p.get_most_mentioned_domain_names(5))
print(p.number_episodes_with_special_guest())
print(p.get_average_duration_episode_in_seconds())