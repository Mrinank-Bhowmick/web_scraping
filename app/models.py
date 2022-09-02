from typing_extensions import Required
from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model

data={'asin':"testing",'title':'mark'}

class Product(Model):                      # --> table name is product
    __keyspace__ = 'scraper_app' 

    asin=columns.Text(primary_key=True,required=True)   # asin is amazon product id
    title=columns.Text()  # title is product title
    price_str=columns.Text()  # price_str is product price

class ProductScrapedEvent(Model):           # --> table name is product_scraped_event
    __keyspace__ = 'scraper_app' 
    uuid=columns.UUID(partition_key=True,required=True) 
    asin=columns.Text(index=True)   # asin is amazon product id
    title=columns.Text()  # title is product title
    price_str=columns.Text()  # price_str is product price

