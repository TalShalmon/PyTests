import re
import sys
from src.URLData import URLData


class DomainUtility:
    @staticmethod
    def is_same_domain(url: URLData, domain):
        return url.domain == domain

    @staticmethod
    def calc_url_domain(url: URLData, extracting_method):
        try:
            pattern = re.compile(extracting_method)
            return re.search(pattern, url).group(0)
        except Exception:
            print('Error - in calc_url_domain for input:' + url, file=sys.stderr)
            return None

    @staticmethod
    def calc_ratio_and_get_sub_urls(url: URLData, content: str, searching_method, extracting_method):
        try:
            pattern = re.compile(searching_method)
            res = []
            for inner_url in re.findall(pattern, content):
                res.append(inner_url)
            counter = 0
            for inner_url in res:
                if DomainUtility.is_same_domain(url, DomainUtility.calc_url_domain(inner_url, extracting_method)):
                    counter += 1
            if res:
                url.set_ratio(counter / len(res))
            return res
        except Exception:
            return []
