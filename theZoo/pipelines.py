# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter

from sqlalchemy.orm import sessionmaker
from theZoo.models import Items, create_items_table, db_connect
from scrapy.exporters import JsonItemExporter



class ThezooPipeline:
    def __init__(self):
        """
        Initializes database connection and sessionmaker.
        Creates items table.
        """
        engine = db_connect()
        create_items_table(engine)
        self.Session = sessionmaker(bind=engine)

    
    file = None

    def open_spider(self, spider):
        self.file = open('item.json', 'wb')
        self.exporter = JsonItemExporter(self.file)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        """
        Here we are processing our item and storing to the database
        """
        self.exporter.export_item(item)

        session = self.Session()
        # instance = session.query(Items).filter_by(**item).one_or_none()
        # if instance:
        #     return instance
        scrape_item = Items(**item)

        try:
            session.add(scrape_item)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

        return item
