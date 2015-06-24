# -*- coding: UTF-8 -*-

__author__ = 'klein'

import config
import requests
from BeautifulSoup import BeautifulSoup

logger = config.getLogger("name1", config.logging.DEBUG)

if __name__ == '__main__':
    response = requests.get(config.url)
    soup = BeautifulSoup(response.text)

    print soup

