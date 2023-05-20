import csv
import json


def csv_to_json(csv_path, json_path):
    data = []

    with open(csv_path, "r") as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            data.append(row)

    with open(json_path, "w") as jsonfile:
        jsonfile.write(json.dumps(data, indent=4))


# Serialisation

csv_path = "fixtures/requete_collecte.csv"
json_path = "fixtures/requete_collecte.json"
csv_to_json(csv_path, json_path)
