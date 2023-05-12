from src.functions.handlers.fileHandler import *
import json

with open(QA_DIR, "r", encoding="utf-8") as f:
    QnA = json.load(f)