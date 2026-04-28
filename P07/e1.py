import http.client
import json

SERVER = 'rest.ensembl.org'
ENDPOINT = '/info/ping'
PARAMS = '?content-type=application/json'
URL = SERVER + ENDPOINT + PARAMS

print()
print(f"Server: {SERVER}")
print(f"URL: {URL}")

connect = http.client.HTTPConnection(SERVER)

try:
    connect.request("GET", ENDPOINT + PARAMS)
    response = connect.getresponse()
    data = json.loads(response.read().decode())

    print(f"Response received!: {response.status} {response.reason}\n")

    if data["ping"] == 1:
        print("PING OK! The database is running|")

except ConnectionRefusedError:
    print('ERROR! Cannot connect to the server')
    exit()




