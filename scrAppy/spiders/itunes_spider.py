from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector

from scrAppy.items import ScrAppyItem

class ITunesSpider(CrawlSpider):
    name = "itunes"
    allowed_domains = ['itunes.apple.com']

    start_urls = ['http://itunes.apple.com/us/genre/ios-navigation/id6010?mt=8&letter=A']
    
    rules = (
        # Extract all the app pages
        Rule(SgmlLinkExtractor(allow=(r'.*/app/.*',), unique=True), 'parse_app', follow=True),
        # Find the different numbered pages:
        Rule(SgmlLinkExtractor(allow=(r'.*letter=[A-Z#]$',)), follow=True),
        Rule(SgmlLinkExtractor(allow=(r'.*page=[0-9]+#page$',)), follow=True),
    )
    
    def parse_app( self, response ):
        hxs = HtmlXPathSelector(response)
        app = ScrAppyItem()
        #self.log('This is another page: %s' % response.url)
        title = hxs.select('//div[@id="title"]/h1/text()').extract()[0]
        image_url = hxs.select('//div[@class="artwork"]/img[@width="175"]/@src').extract()[0]
        appID = response.url.split("/")[-1].split("?")[0]
        app['title'] = title
        app['image_url'] = image_url
        app['appID'] = appID
        self.log('App: %s' % app)