import http.client
import json
import termcolor

SERVER = 'rest.ensembl.org'
conn = http.client.HTTPConnection(SERVER)

gene_list = ['FRAT1', 'ADA', 'FXN', 'RNU6-269P', 'MIR633', 'TTTY4C', 'RBMY2YP', 'FGFR3', 'KDR', 'ANK2']
gene_dict = {}

print("\nDictionary of Genes!")
print(f"There are {len(gene_list)} genes in the dictionary:\n")

for gene in gene_list:
    endpoint = f"/lookup/symbol/homo_sapiens/{gene}?content-type=application/json"

    try:
        conn.request("GET", endpoint)
        response = conn.getresponse()

        if response.status == 200:
            data = json.loads(response.read().decode())
            gene_id = data['id']
            gene_dict[gene] = gene_id
            termcolor.cprint(f"{gene}:", "yellow", end="")
            print(f" --> {gene_id}")
        else:
            print(f"Gene {gene} not found")

    except ConnectionRefusedError:
        print('ERROR! Cannot connect to the server')
        exit()











