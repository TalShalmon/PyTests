# Web Crawler
## About
When analyzing web pages relationship is very useful to have 'Page Rank' that measure how single web page is demonstrating specific character/property.
In this example we would look at self-domain module for this ranking system.
I created it as easy as possible to adjust, so you could implement any 'weight' function you desired for ranking web pages.

## Design
The crawler implementation includes main logic class, called 'Crawler' (CrawlerLogic.py) and it's where the
main end-point that expose the app. the method 'crawl' will initiate the crawling process from the given root web page 
and will run 2 phases in the following order: 
1. validation
2. execution
 
In execution step we use implementation of BFS algorithm for iterate the web pages properly. The Domain object called 
'URLData' and store all required information about single web-page. The Functionality using this object and some simple
DS for the solution is in DomainUtility. The behavior of the crawl is determined in Strategy object that implement 2
strategies Online/Offline crawling. Default behavior is online.

Tests with simple configurations can be found in class 'CrawlerBaseTest'.

## Getting Started
#### Prerequisites
	- Python
		○ Pip install / apt-get / any installation CMD
	- Installation:
		○ Git clone

## Usage
- Python command: WebCrawler/web_crawler.py <URL> <DEPTH>
- Go to file 'web_crawler.py' and execute main.
- Go to file 'CrawlerBaseTest.py' and run tests.