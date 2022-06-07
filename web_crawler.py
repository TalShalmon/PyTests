import sys
from src import CrawlerLogic


if __name__ == '__main__':
    try:
        x = CrawlerLogic.Crawler(sys.argv[1], sys.argv[2])
        print(x.crawl())
    except ValueError as v:
        print('failed execute web crawler due to illegal depth argument. cause: ', v)
    except Exception as e:
        print('failed execute web crawler. cause: ', e)
