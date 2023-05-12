import os

ROOT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..'))
print(f"Root directory: {ROOT_DIR}")
JSON_DIR = os.path.join(ROOT_DIR, 'src', 'src', 'json')
print(f"JSON directory: {JSON_DIR}")
QA_DIR =  os.path.join(JSON_DIR, 'QnA.json')
print(f"QA directory: {QA_DIR}")