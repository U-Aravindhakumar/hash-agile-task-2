import csv
from elasticsearch import Elasticsearch
es = Elasticsearch("http://localhost:9200")
with open('employee_sample_data.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        es.index(index='employee_data', body=row)
print("Employee data indexed.")
res = es.search(index="employee_data", body={"query": {"match_all": {}}})
print("Search Results:", res['hits']['hits'])
