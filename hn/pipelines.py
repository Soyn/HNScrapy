from sqlalchemy.orm import sessionmaker
from models import Hn, db_connect, create_hn_table

class HnPipeline(object):
    def __init__(self):
        engine = db_connect()
        create_hn_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        session = self.Session()
        hn = Hn(**item)
        session.merge(hn)
        session.commit()
        return item