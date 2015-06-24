__author__ = 'klein'

import config

print config.url

logger = config.getLogger("name1", config.logging.DEBUG)

logger.info(config.url)

