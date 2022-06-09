from src.DomainUtility import DomainUtility
from src.Errors import CrawlerError
from src.URLData import URLData
from src.URLStrategy import URLStrategy
from src.URLStrategy.OnlineParser import OnlineParser

DEPTH_MAX_VALUE = 100


class Crawler:
    url_fetch_strategy: URLStrategy.URLStrategy

    def __init__(self, url, depth, url_fetch_strategy: URLStrategy):
        self.root_url = url
        self.depth = depth
        self.depth_numeric = 0
        if url_fetch_strategy is None:
            self.url_fetch_strategy = OnlineParser()
        else:
            self.url_fetch_strategy = url_fetch_strategy

    def crawl(self) -> str:
        self.prepare_crawl_action()
        return create_tsv(self.calculate_result())

    def prepare_crawl_action(self):
        try:
            depth_value = int(self.depth)
            self.depth_numeric = depth_value
        except ValueError as v:
            raise CrawlerError('failed execute web crawler due to illegal depth argument. cause: ', v)
        if depth_value < 0 or depth_value > DEPTH_MAX_VALUE:
            raise Exception('Illegal Depth')
        if not self.url_fetch_strategy.is_valid_url(self.root_url):
            raise Exception('Illegal URL')

    def calculate_result(self) -> str:
        visited = set()
        visited.add(self.root_url)

        res = []
        root_element = URLData(self.root_url, 0, DomainUtility.calc_url_domain(self.root_url, self.url_fetch_strategy.get_regex_for_domain_extract()))
        next_level = [root_element]

        for current_depth in range(1, self.depth_numeric + 1):
            next_iteration_urls = set()
            for url in next_level:
                sub_urls = DomainUtility.calc_ratio_and_get_sub_urls(url, self.url_fetch_strategy.parse(url.get_url()),
                                                                     self.url_fetch_strategy.get_regex_for_url_search(),
                                                                     self.url_fetch_strategy.get_regex_for_domain_extract())
                res.append(url)
                next_iteration_urls.update(sub_urls)

            next_level = set()
            for url in next_iteration_urls:
                if url not in visited:
                    next_level.add(URLData(url, current_depth, DomainUtility.calc_url_domain(url, self.url_fetch_strategy.get_regex_for_domain_extract())))
                    visited.add(url)
        return res


def create_tsv(urls_list) -> str:
    res = "url\tdepth\tratio"
    for url in urls_list:
        res += "\n" + url.url + "\t" + str(url.get_depth()) + "\t" + str(url.get_ratio())
    return res
