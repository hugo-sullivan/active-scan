# pScan
Active scanning tool for research, to be used with a passive inferencing tool for characterization of IoT devices through less common packet types.
## Description
pScan was created to make it easier for researchers working on passive inferencing tools to send more obscure packets for the sake of characterising IoT devices. To accomidate this pScan was made to be very modular so that additional packet types could easily be added, only needing a single file to be added and without changing any pre-existing code. 
The project pScan itself cannot process or return results from scans that it runs, this is why it is meant to be used with a passive inferincing tool which is capable of processing the packets and infering information from them. The point of pScan is soley to provide a simple to use API that can send less common packet types for researching into passive inferencing.

Python was used with this project because it is meant for testing at small scales, so we used a language which could be quickly added to with additional packet types.

## Setup Guide
Requires python 3.8-3.10

Multiple packets need to be installed so a python package installer is helpful I recommend pip.

The python packages required are

- pysnmp
- ssdpy
- nmap3
- zeroconf
- flask
- flask_swagger_ui
- flasgger


These are listed in requirement.txt and can all be installed with pip using the command

**python -m pip install -r requirements.txt**


The tool nmap also has to be installed, it can be installed here https://nmap.org/download.


The Server uses HTTPS so a cert.pem file and key.pem file have to be saved to the base directory, to generate your own SSL certificate I recommend using the program openssl. 

To add and delete scans an API Key is required this should be entered in the configuration.yaml file and sent with the rest of the API call.
## Usage
To run the tool, run the program app.py then API calls can be made to it.

Instructions on the API is include in the swagger.yaml file to access this, run the app.py program and visit the page http://127.0.0.1:5000/swagger/, which will provide information on the different API calls and schemas that are used.

To add additional modules:
* the file has to be added to the directory *Modules*. 
* They have to implement *ScannerForm* class in the *ScanInterface* file.
* The class in the new module file must be called *scanner*
* This new class requires the same *__init__* function as the other modules.
* The function *get_name* will return the name that has to  be put in the *type* section to call this function from the API.

