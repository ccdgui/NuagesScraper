from scrapy.loader import ItemLoader
from scrapy.spiders import CrawlSpider
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from MigraineCloud.items import ForumCloudItem

class ForumSpider(CrawlSpider):
    name = 'NuagesForum'
    allowed_domains = ['patient.info']

    start_urls = ['https://patient.info/forums/discuss/browse/migraine-1415'] 

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//*[@class='post thread']//h3//a"), callback="follow"), 
    )

    def follow(self, response):
        node0 = response.xpath('//span[@class="avt-usr"]').extract()[0]
        thread_id = response.xpath("//article[@class='post mb-0']//@data-d").extract()[0]
        bubble_id = thread_id+str(0)
        item_loader = ItemLoader(item=ForumCloudItem(), selector=response)
        item_loader.add_value('bubble_id', bubble_id)
        item_loader.add_xpath('bubble_title', '//*[@class="post-title"]')
        item_loader.add_value('node0', node0)
        item_loader.add_value('node1', node0)
        item_loader.add_value('node2', node0)
        item_loader.add_xpath('bubble_content', "//div[@id='post_content']//p")
        return item_loader.load_item()
