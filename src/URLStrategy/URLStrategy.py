from abc import ABC, abstractmethod


class URLStrategy(ABC):
    @abstractmethod
    def parse(self, target: str):
        pass

    @abstractmethod
    def is_valid_url(self, url: str):
        pass

    @abstractmethod
    def get_regex_for_url_search(self):
        pass

    @abstractmethod
    def get_regex_for_domain_extract(self):
        pass
