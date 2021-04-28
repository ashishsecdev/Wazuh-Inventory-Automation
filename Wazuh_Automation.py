import requests
import json
import csv


url = "http://Wazuh-Endpoint.com:PortNumber"
agentNames = "/agents"
URL = url + agentNames
user = '<UserName>'
password= '<PassWord>'

response = requests.get(URL, verify=False, auth=(user, password))
r = json.loads(response.text)
for i in r["data"]["items"]:
    agentlist = i["id"]
    endpoint = "/syscollector/" + agentlist + "/processes"
    second = url + endpoint
    response = requests.get(second, verify=False, auth=(user, password))
    r = json.loads(response.text)
    for i in r["data"]["items"]:
        with open('Wazuh_Inventory.csv', mode='a') as csv_file:
            fieldnames = ['Process Name', 'PID', "Agent Name"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writerow({'Process Name': i["name"], 'PID': i["pid"], 'Agent Name':agentlist})
