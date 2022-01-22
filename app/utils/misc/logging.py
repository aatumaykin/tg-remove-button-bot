import logging

from app.utils import config

logging.basicConfig(
    level=config.LOG_LEVEL,
    format=u'%(asctime)s - %(levelname)s:%(name)s:%(message)s'
)
