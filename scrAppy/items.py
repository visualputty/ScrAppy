# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class ScrAppyItem(Item):
    # define the fields for your item here like:
    title = Field()
    appID = Field()
    image_urls = Field()
    images = Field()
    pass
