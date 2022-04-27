import requests
import json
import csv
import urllib3
from base64 import b64encode

# Disable insecure https warnings (for self-signed SSL certificates)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Configuration
protocol = 'https'
host = 'localhost'
port = 55000
user = 'wazuh_api_user'
password = 'wazuh_api_password'

#Establish API facts
base_url = f"{protocol}://{host}:{port}"
agentnames_endpoint = "/agents"
agentnames_url = base_url + agentnames_endpoint

#login
login_endpoint = 'security/user/authenticate'
login_url = f"{protocol}://{host}:{port}/{login_endpoint}"
basic_auth = f"{user}:{password}".encode()
login_headers = {'Content-Type': 'application/json',
                 'Authorization': f'Basic {b64encode(basic_auth).decode()}'}
print("\nLogin ...\n")
response = requests.get(login_url, headers=login_headers, verify=False)
token = json.loads(response.content.decode())['data']['token']

# New authorization header with the JWT token we got
requests_headers = {'Content-Type': 'application/json',
                    'Authorization': f'Bearer {token}'}
# Start Inventory
print("\nStart Inventory ...\n")
response = requests.get(agentnames_url, headers=requests_headers, verify=False)

r = json.loads(response.text)
for i in r["data"]["affected_items"]:
    agentlist = i["id"]
    agentname = i["name"]
    endpoint = "/syscollector/" + agentlist + "/processes"
    second = base_url + endpoint
    response = requests.get(second, headers=requests_headers, verify=False)
    r = json.loads(response.text)
    for i in r["data"]["affected_items"]:
        with open('Wazuh_Inventory.csv', mode='a') as csv_file:
            fieldnames = ['Process Name', 'PID', "Agent Name"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writerow({'Process Name': i["name"], 'PID': i["pid"], 'Agent Name':agentname})
print("\nInventory Complete ...\n")
