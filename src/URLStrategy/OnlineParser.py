import re
import sys
import urllib.request
from urllib.error import HTTPError
from src.URLStrategy.URLStrategy import URLStrategy


class OnlineParser(URLStrategy):
    def __init__(self):
        self.regex_for_link_search = re.compile(r'a href[ ]{0,1}=[ ]{0,1}"(http(?:s)?(?:[^\"]{0,}))"')
        self.regex_for_domain_extract = re.compile(r'^(?:http(s?):\/\/)([A-Z0-9a-z.])*')
        self.regex_for_url_validity = re.compile(
            r'^(?:http)s?://'
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
            r'localhost|'
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
            r'(?::\d+)?'
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    def is_valid_url(self, url: str):
        return re.match(self.regex_for_url_validity, url) is not None

    def parse(self, target: str):
        try:
            page = urllib.request.urlopen(target)
            data = page.read()
            return data.decode('utf-8')
        except HTTPError as http_error:
            print('Connection error on fetch data', file=sys.stderr)
        except Exception:
            print('general error on fetch data', file=sys.stderr)

    def get_regex_for_url_search(self):
        return self.regex_for_link_search

    def get_regex_for_domain_extract(self):
        return self.regex_for_domain_extract
