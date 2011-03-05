# Scrapy settings for scrAppy project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'scrAppy'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['scrAppy.spiders']
NEWSPIDER_MODULE = 'scrAppy.spiders'
DEFAULT_ITEM_CLASS = 'scrAppy.items.ScrappyItem'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

