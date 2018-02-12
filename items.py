import scrapy
from scrapy.loader.processors import TakeFirst, MapCompose
from w3lib.html import remove_tags


class ForumCloudItem(scrapy.Item):
    bubble_id = scrapy.Field(
        input_processor=MapCompose(remove_tags)
        )
    bubble_title = scrapy.Field(
        input_processor=MapCompose(remove_tags),
        output_processor=TakeFirst()
        )
    node0 = scrapy.Field(
        input_processor=MapCompose(remove_tags),
        output_processor=TakeFirst()
        )
    node1 = scrapy.Field(
        input_processor=MapCompose(remove_tags),
        output_processor=TakeFirst()
        )
    node2 = scrapy.Field(
        input_processor=MapCompose(remove_tags),
        output_processor=TakeFirst()
        )
    bubble_content = scrapy.Field(
        input_processor=MapCompose(remove_tags)
        )
