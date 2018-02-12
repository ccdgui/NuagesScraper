from scrapy.exporters import JsonItemExporter

class MigrainecloudPipeline(object):
    def __init__(self):
        self.file = open("graph_analysis", 'wb')
        self.exporter = JsonItemExporter(self.file, encoding='utf-8')
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

