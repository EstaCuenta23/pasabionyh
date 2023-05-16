from src.functions.handlers.loggingHandler import *

import os

ROOT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
JSON_DIR = os.path.join(ROOT_DIR, 'db', 'json')
QA_DIR =  os.path.join(JSON_DIR, 'QnA', 'QnA.json')

logging.info(f"Root directory: {ROOT_DIR}")
logging.info(f"JSON directory: {JSON_DIR}")
logging.info(f"QnA directory: {QA_DIR}")