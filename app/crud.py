import uuid
import copy
from .db import get_session
from .models import Product,ProductScrapedEvent
from cassandra.cqlengine.management import sync_table


session=get_session()


# this will update an existing entry in the table with the new data provided in the dict argument 
sync_table(Product)
sync_table(ProductScrapedEvent) 

data={
"asin": "BCQsdfs",
"title": "mark 321"
}
def create_entry(data:dict):                # this will create a new entry in the table
    return Product.create(**data)


def create_scraped_entry(data:dict):        # this will create a new items to our database 
    data['uuid'] = uuid.uuid1() # uuid1 includes a timestamp  
    return ProductScrapedEvent.create(**data)

def add_scrape_event(data:dict,fresh=False):
    if fresh:
        data=copy.deepcopy(data)
    product=create_entry(data)
    scrape_object=create_scraped_entry(data)
    return product,scrape_object