import re


class DomainException(Exception):
    """Raised when an invalid is created."""


class Domain:

    def __init__(self, name):
        # validate a current domain (r'.*\.[a-z]{2,3}$' is fine)
        # if not valid, raise a DomainException
        self.name = name
        if not re.findall(r'.*\.[a-z]{2,3}$', self.name):
            raise DomainException
    
    def __str__(self):
        return self.name
    

    @classmethod
    def parse_from_url(cls,url):
        url = re.search(r'https?://(\w+)(\.\w+)', url)
        return cls(''.join(url.group(1,2)))

    
    @classmethod
    def parse_from_email(cls, email):
        cls.email = re.search(r'([\w\W]+@)([\w\W]+)',email)
        return cls(cls.email.group(2))
        
    # next add a __str__ method and write 2 class methods
    # called parse_from_url and parse_from_email to construct domains
    # from an URL and email respectively

d = Domain('http://google.com')
#print(d.parse_from_url('https://python.org/'))
print(d.parse_from_email('sara@hotmail.co.uk'))
domain = Domain.parse_from_email('sara@hotmail.co.uk')
print(type(domain))
domain2 = Domain.parse_from_url('https://python.org/')
print(type(domain2))
print(Domain.parse_from_url('http://pybit.es'))