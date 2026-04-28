import http.client
import json
import termcolor

SERVER = 'rest.ensembl.org'
conn = http.client.HTTPConnection(SERVER)

gene = 'MIR633'

endpoint1 = f"/lookup/symbol/homo_sapiens/{gene}?content-type=application/json"

conn.request("GET", endpoint1)
response1 = conn.getresponse()

data1 = json.loads(response1.read().decode())
gene_id = data1['id']
print(gene_id)

endpoint2 = f'/sequence/id/{gene_id}?content-type=application/json'

conn.request("GET", endpoint2)
response2 = conn.getresponse()

data2 = json.loads(response2.read().decode())
gene_seq = data2['seq']

print(f"Server: {SERVER}"





