BOT_NAME = 'hn'

SPIDER_MODULES = ['hn.spiders']
NEWSPIDER_MODULE = 'hn.spiders'

DATABASE = {'drivername': '',
            'username': '',
            'password': '',
            'database': ''}

ITEM_PIPELINES = {
    'hn.pipelines.HnPipeline':300
}
