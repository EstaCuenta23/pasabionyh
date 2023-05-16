import os
import logging

log_file = 'data/logs/pasabio.log'
if os.path.isfile(log_file):
    open(log_file, 'w').close()

logging.basicConfig(filename=log_file, level=logging.INFO, encoding="utf-8")