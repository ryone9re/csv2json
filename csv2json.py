import csv
import json
import sys

json_list = []
fp = sys.argv[1]

with open(fp, 'r', encoding="utf_8_sig") as f:
    for row in csv.DictReader(f):
        json_list.append(row)

with open('output.json', 'w', encoding="utf_8_sig") as f:
    json.dump(json_list, f, ensure_ascii=False)
