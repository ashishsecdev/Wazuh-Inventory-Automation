# Wazuh-Inventory-Automation

This script fetches the inventory information of all Wazuh agents via with processes and PIDs

Currently, Wazuh does not have the functionality of tracking Wazuh Agents invetory one by one, so manual effort is required to get the list of running processes and packages.

This script will user Wazuh Api to fetch the list of registered agents and will then save the inventory details one by one in CSV. 

You can limit the output of the script using the current status of agents like **"status": "Active"** or **"status": "Never connected"**

Requirement:

1. Wazuh API credentials.
2. Python 3.0 with Request and CSV module.


Please feel free to open issue if you face any issue with the script.

~Asecdev
