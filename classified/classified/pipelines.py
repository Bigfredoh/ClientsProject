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
        if adapter["title"] is self.title_seen:
            raise DropItem(f'Duplicate ad detected {item}')
        else:
            self.title_seen.add(adapter["title"])
            return item
class ClassifiedRemovedNoPhonesPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        if not adapter["landline"] and not adapter["mobile"]:
            raise DropItem(f'ad with no contact info detected {item}')
        else:
            return item

class MongoPipeline:
    collection_name = 'classified'
    def __init__(self, mongodb_url, mongodb):
        pass

