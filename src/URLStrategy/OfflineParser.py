import re
from definitions import ROOT_DIR
from src.URLStrategy.URLStrategy import URLStrategy


class OfflineParser(URLStrategy):
    def __init__(self):
        self.regex_for_link_search = re.compile(r'(?:href[ ]{0,1}=")([^\"]{0,})"')
        self.regex_for_domain_extract = re.compile(r'.*(?:\/)')

    def is_valid_url(self, url: str):
        return True

    def parse(self, target: str):
        with open(ROOT_DIR + target, 'r') as page:
            return page.read().rstrip()

    def get_regex_for_link_validation(self):
        return self.regex_for_link_search

    def get_regex_for_domain_extract(self):
        return self.regex_for_domain_extract
