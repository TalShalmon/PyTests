import unittest
from src import CrawlerLogic
from src.URLStrategy import OfflineParser, OnlineParser

TEST_URL_OFFLINE = '/tests/pages/a.html'
TEST_URL_ONLINE = 'https://news.ycombinator.com'
TEST_DEPTH = '3'


class CrawlerBaseTest(unittest.TestCase):
    @staticmethod
    def create_test_offline_crawler():
        return CrawlerLogic.Crawler(TEST_URL_OFFLINE, TEST_DEPTH, OfflineParser.OfflineParser())

    @staticmethod
    def create_test_online_crawler():
        return CrawlerLogic.Crawler(TEST_URL_ONLINE, TEST_DEPTH, OnlineParser.OnlineParser())

    def test_offline(self):
        test_crawler = self.create_test_offline_crawler()
        res = test_crawler.crawl()
        print(res)
        self.assertTrue(res is not None)

    def test_online(self):
        test_crawler = self.create_test_online_crawler()
        res = test_crawler.crawl()
        print(res)
        self.assertTrue(res is not None)
