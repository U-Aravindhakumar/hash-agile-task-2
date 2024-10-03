from elasticsearch import Elasticsearch
client = Elasticsearch("http://localhost:9200")
index_name = 'employee_data'
client.indices.create(index=index_name, ignore=400)
print(f"Index '{index_name}' created.")

