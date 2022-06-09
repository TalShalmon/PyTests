class URLData:
    def __init__(self, url: str, depth: int, domain: str):
        self.url = url
        self.depth = depth
        self.ratio = 0
        # self.url_searching = url_search_regex
        # self.domain_extract = url_extractor_regex
        self.domain = domain

    def get_depth(self):
        return self.depth

    def get_url(self):
        return self.url

    def get_ratio(self):
        return self.ratio

    def set_ratio(self, ratio):
        self.ratio = ratio

    def get_domain(self):
        return self.domain

    # def get_domain_extracting(self):
    #     return self.domain_extract
    #
    # def get_url_searching(self):
    #     return self.url_searching





