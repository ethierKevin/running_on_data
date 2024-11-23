import csv

def parse_csv(file_stream):
    data = []
    csv_reader = csv.DictReader(file_stream)
    for row in csv_reader:
        data.append(row)
    return data