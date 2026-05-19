import http.server
import http.client
import socketserver
import json
from pathlib import Path
from urllib.parse import parse_qs, urlparse
import jinja2 as j

PORT = 8080
socketserver.TCPServer.allow_reuse_address = True

SERVER = 'rest.ensembl.org'
params = '?content-type=application/json'

class TestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        contents = ""

        url_path = urlparse(self.path)
        path = url_path.path
        arguments = parse_qs(url_path.query)

        def read_html_file(filename):
            contents = Path("html/" + filename).read_text()
            contents = j.Template(contents)
            return contents

        if path == "/" or path == "/index.html":
            self.send_response(200)
            contents = read_html_file("index.html").render()

        elif path == "/listSpecies":
            self.send_response(200)
            arg_limit = arguments.get("limit", [None])[0]
            if arg_limit is None or arg_limit == "":
                limit = None
            else:
                limit = int(arg_limit)

            endpoint1 = '/info/species'

            connect = http.client.HTTPConnection(SERVER)

            try:
                connect.request("GET", endpoint1 + params)
                response = connect.getresponse()

                data = json.loads(response.read().decode())

                all_species = data["species"]

                total_species = len(all_species)

                species_list = []
                for sp in all_species:
                    species_list.append(sp["display_name"])

                if limit is None:
                    final_list = species_list
                else:
                    final_list =species_list[:limit]

                contents = read_html_file("SpeciesList.html").render(limit=limit, species_list=final_list, total_species=total_species)

            except ConnectionRefusedError:
                print('ERROR! Cannot connect to the server')
                exit()


        elif path == "/karyotype":
            self.send_response(200)
            species = arguments.get("species", ["human"])[0]

            endpoint2 = f"/info/assembly/{species}"

            connect = http.client.HTTPConnection(SERVER)

            try:
                connect.request("GET", endpoint2 + params)
                response = connect.getresponse()

                if response.status != 200:
                    print(f"The species '{species}' was not found in the Ensembl database.")
                    contents = read_html_file("error.html").render()

                else:
                    data = json.loads(response.read().decode())

                    regions = data["top_level_region"]
                    karyotype = []
                    for region in regions:
                        if region["coord_system"] == "chromosome":
                            karyotype.append(region["name"])

                    contents = read_html_file("InfoKaryotype.html").render(species=species, karyo_info=karyotype)

            except ConnectionRefusedError:
                print('ERROR! Cannot connect to the server')
                exit()


        elif path == "/chromosomeLength":
            self.send_response(200)
            species = arguments.get("species", ["human"])[0]
            chromosome = arguments.get("chromo", ["1"])[0]

            endpoint3 = f"/info/assembly/{species}"

            connect = http.client.HTTPConnection(SERVER)

            try:
                connect.request("GET", endpoint3 + params)
                response = connect.getresponse()
                if response.status != 200:
                    print(f"The species '{species}' or the chromosome '{chromosome} were not found in the Ensembl database.")
                    contents = read_html_file("error.html").render()

                else:
                    data = json.loads(response.read().decode())

                    regions = data["top_level_region"]

                    chromosome_length = None

                    for region in regions:
                        if str(region["name"]).strip(" ") == chromosome.upper():
                            chromosome_length = region["length"]
                            break

                    contents = read_html_file("ChromosomeLength.html").render(species=species, chromo=chromosome,
                                                                              chromo_length=chromosome_length)

            except ConnectionRefusedError:
                print('ERROR! Cannot connect to the server')
                exit()


        elif path == "/geneLookup":
            self.send_response(200)
            gene = arguments.get("gene_name", [])[0]

            endpoint4 = f"/lookup/symbol/homo_sapiens/{gene}"

            connect = http.client.HTTPConnection(SERVER)

            try:
                connect.request("GET", endpoint4 + params)
                response = connect.getresponse()
                if response.status != 200:
                    print(f"The gene '{gene}' or the chromosome was not found in the Ensembl database.")
                    contents = read_html_file("error.html").render()

                else:
                    data = json.loads(response.read().decode())

                    gene_id = data["id"]

                    contents = read_html_file("GeneId.html").render(gene_name=gene,gene_id=gene_id)

            except ConnectionRefusedError:
                print('ERROR! Cannot connect to the server')
                exit()

        elif path == "/geneSeq":
            self.send_response(200)

            gene = arguments.get("gene_name", [""])[0].strip(" ")

            endpoint5_1 = f"/lookup/symbol/homo_sapiens/{gene}"
            connect = http.client.HTTPConnection(SERVER)

            try:
                connect.request("GET", endpoint5_1 + params)
                response = connect.getresponse()

                if response.status != 200:
                    print(f"The gene '{gene}' was not found in the Ensembl database.")
                    contents = read_html_file("error.html").render()

                else:
                    data = json.loads(response.read().decode())
                    gene_id = data["id"]

                    endpoint5_2 = f"/sequence/id/{gene_id}"

                    try:
                        connect.request("GET", endpoint5_2 + params)
                        response2 = connect.getresponse()

                        if response2.status != 200:
                            print(f"The sequence for gene '{gene}' (ID: {gene_id}) could not be retrieved.")
                            contents = read_html_file("error.html").render()

                        else:
                            data_seq = json.loads(response2.read().decode())
                            seq = data_seq['seq']

                            contents = read_html_file("GeneSequence.html").render(gene_name=gene,gene_sequence=seq)

                    except ConnectionRefusedError:
                        print('ERROR! Cannot connect to the server during step 2')
                        exit()

            except ConnectionRefusedError:
                print('ERROR! Cannot connect to the server during step 1')
                exit()


        elif path == "/geneInfo":
            self.send_response(200)

            gene = arguments.get("gene_name", [""])[0].strip(" ")

            endpoint6 = f"/lookup/symbol/homo_sapiens/{gene}"

            connect = http.client.HTTPConnection(SERVER)

            try:
                connect.request("GET", endpoint6 + params)
                response = connect.getresponse()

                if response.status != 200:
                    print(f"The gene '{gene}' was not found in the Ensembl database.")
                    contents = read_html_file("error.html").render()

                else:
                    data = json.loads(response.read().decode())

                    gene_start = data["start"]
                    gene_end = data["end"]
                    gene_length = gene_end - gene_start
                    gene_id = data["id"]
                    chromosome_name = data["seq_region_name"]

                    contents = read_html_file("GeneInfo.html").render(gene_name=gene, start=gene_start, end=gene_end, length=gene_length, id=gene_id, chromo=chromosome_name)

            except ConnectionRefusedError:
                print('ERROR! Cannot connect to the server during step 1')
                exit()


        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', str(len(contents.encode())))
        self.end_headers()
        self.wfile.write(contents.encode())


Handler = TestHandler
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at PORT", PORT)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped by the user")
        httpd.server_close()