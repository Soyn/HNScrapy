from scrapy.item import Item, Field

class HnItem(Item):
    title = Field()
    link = Field()
