BOT_NAME = 'hn'

SPIDER_MODULES = ['hn.spiders']
NEWSPIDER_MODULE = 'hn.spiders'

DATABASE = {'drivername': 'postgres',
            'username': 'ajay',
            'password': '12345',
            'database': 'hn'}

ITEM_PIPELINES = {
    'hn.pipelines.HnPipeline':300
}
