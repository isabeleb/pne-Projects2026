import http.client
import json
import termcolor
from Seq7 import Seq

SERVER = 'rest.ensembl.org'
conn = http.client.HTTPConnection(SERVER)

gene_list = ['FRAT1', 'ADA', 'FXN', 'RNU6-269P', 'MIR633', 'TTTY4C', 'RBMY2YP', 'FGFR3', 'KDR', 'ANK2']

for gene in gene_list:
    endpoint1 = f'/lookup/symbol/homo_sapiens/{gene}'
    params1 = '?content-type=application/json'

    try:
        conn.request("GET", endpoint1 + params1)
        response1 = conn.getresponse()

        data1 = json.loads(response1.read().decode())
        gene_id = data1['id']

        endpoint2 = f'/sequence/id/{gene_id}'
        params2 = '?content-type=application/json'
        conn.request("GET", endpoint2 + params2)
        response2 = conn.getresponse()

        data2 = json.loads(response2.read().decode())
        gene_seq = data2['seq']

        endpoint3 = f'/sequence/id/{gene_id}'
        params3 = '?content-type=text/x-fasta;expand_5prime=10;type=genomic'
        conn.request("GET", endpoint3 + params3)
        response3 = conn.getresponse()

        data3 = response3.read().decode()
        gene_description_list = data3.split(' ')
        gene_description_first_lines = gene_description_list[1].splitlines()
        gene_description = gene_description_first_lines[0]

        print(f"\nServer: {SERVER}")
        print(f"URL: {SERVER + endpoint2 + params2}")
        print(f"Response received!: {response2.status} {response2.reason}\n")

        termcolor.cprint('Gene: ', 'yellow', end='')
        print(gene)
        termcolor.cprint('Description: ', 'yellow', end='')
        print(gene_description)

        sequence = Seq(gene_seq)

        bases_count_dict = sequence.count_base()

        termcolor.cprint('Total length: ', 'yellow', end='')
        print(sequence.len())

        for base, count in bases_count_dict.items():
            termcolor.cprint(f'{base}: ', 'blue', end='')
            print(count)

        mf_base_count = 0
        most_freq_base = None

        for b, c in bases_count_dict.items():
            count = int(c)
            if count > mf_base_count:
                mf_base_count = count
                most_freq_base = b
        termcolor.cprint('Most frequent base: ', 'yellow', end='')
        print(most_freq_base)

    except ConnectionRefusedError:
        print('ERROR! Cannot connect to the Server')
        exit()



