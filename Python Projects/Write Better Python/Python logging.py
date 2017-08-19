# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 18:27:13 2017

@author: Monic
"""

# logging

import logging

logging.basicConfig(filename = 'game.log', level = logging.DEBUG)

# CRITICAL, ERROR, WARNING, INFO, DEBUG, NOT SET
# levels of logging

monster = 'booo!'
#log writes monster to the log file
logging.debug(monster)