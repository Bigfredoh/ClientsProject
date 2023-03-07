# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
import pymongo




class ClassifiedRemovedDuplicatesPipeline:

    def __init__(self):
        self.title_seen = set()

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        if adapter["DOB"] is self.title_seen:
            raise DropItem(f'Duplicate ad detected {item}')
        else:
            self.title_seen.add(adapter["DOB"])
            return item
    def process_items(self, item, spider):
        adapter = ItemAdapter(item)
        if adapter["name"] is self.title_seen:
            raise DropItem(f'Duplicate ad detected {item}')
        else:
            self.title_seen.add(adapter["name"])
            return item
    def process_itemss(self, item, spider):
        adapter = ItemAdapter(item)
        if adapter["position"] is self.title_seen:
            raise DropItem(f'Duplicate ad detected {item}')
        else:
            self.title_seen.add(adapter["position"])
            return item

class FantasyPipeline:
    def process_item(self, item, spider):
        return item
