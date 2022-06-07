import re
from src.Errors import CrawlerError


class Crawler:

    def __init__(self, url, depth):
        self.url = url
        self.depth = depth
        self.depth_numeric = 0

    def get_result(self):
        return self.url + '<=>' + str(self.depth)

    def crawl(self):
        self.prepareCrawlAction()
        self.calculate_result()
        return self.getResult()

    def prepare_crawl_action(self):
        try:
            depth_value = int(self.depth)
            self.depth_numeric = depth_value
        except ValueError as v:
            raise CrawlerError('failed execute web crawler due to illegal depth argument. cause: ', v)
        if depth_value < 0 or depth_value > 1000000:
            raise Exception('Illegal Depth')
        if not self.isValidUrl(self.url):
            raise Exception('Illegal URL')

    @staticmethod
    def is_valid_url(url: str):
        regex = re.compile(
            r'^(?:http|ftp)s?://'
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
            r'localhost|'
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
            r'(?::\d+)?'
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)
        return re.match(regex, url) is not None

    def calculate_result(self):
        pass
