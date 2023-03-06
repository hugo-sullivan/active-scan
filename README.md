# pScan
A programmable packet emitter with open APIs that can be dynamically controlled to perform contextualized scans on target (IoT) assets via SNMP, mDNS, and SSDP packets, as well as banner grabbing and probing via TCP connections. It is primarily built to assist researchers who study and develop tools for characterizing target assets while operational costs are kept at a minimum. 
## Description
pScan can be used in conjunction with passive inference tools (see our research paper [[1]](#1)) to characterize IoT devices on a network. This tool dynamically emits specific packets on demand via API calls. pScan sends scan requests (to specified assets) and does not process responses to those request packets. Needless to say, a passive inference tool (the API caller) will ingest scan requests and corresponding responses in conjunction with other packets to/from all networked assets. 

pScan is extensible and currently supports four packet types, namely “TCP banner grabbing”, “SNMP”, “mDNS”, and “SSDP”. To accommodate an additional packet type, one can add only a corresponding file without changing any pre-existing code. 

The tool is written in Python for ease of development and extension. 

## Setup Guide
Requires python 3.8-3.10

Multiple packages need to be installed so a python package installer is helpful I recommend pip. 

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


The tool [Nmap](https://nmap.org/download) also must be installed, it can be found here. 


The Server uses HTTPS. Therefore, two files, namely cert.pem and key.pem, will have to be saved in the base directory. To generate your own SSL certificate, I recommend using openssl. 

To add and delete scans an API Key is required. This should be entered in the configuration.yaml file and sent with each API call. 

## Usage

To run the tool, execute the program app.py. Following that, API calls can be made to it. 

API documentation can be found in the swagger.yaml file. To access this file, run the app.py program and visit the page http://127.0.0.1:5000/swagger/, which will provide information on the different API calls and schemas that are used. 

To extend our tool with additional modules: 

* the file has to be added to the directory *Modules*. 

* They have to implement *ScannerForm* class in the *ScanInterface* file. 

* The class in the new module file must be called *scanner*. 

* This new class requires the same init function as the other modules. 

* The function *get_name* will return the name that has to be put in the *type* section to call this function from the API. 

## References
<a id="1">[1]</a> 
H. Sullivan, A. Sivanathan, A. Hamza, and H. Habibi Gharakheili, "Programmable Active Scans Controlled by Passive Traffic Inference for IoT Asset Characterization", IEEE/IFIP NOMS workshop on Internet of Things Management (Manage-IoT), Miami, FL, USA, May 2023. 
