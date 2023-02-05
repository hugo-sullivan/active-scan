# pScan
Active scanning tool for research, to be used with a passive inferencing tool for characterization of IoT devices through less common packet types.
# Description
pScan was created to make it easier for researchers working on passive inferencing tools to send more obscure packets for the sake of characterising IoT devices. To accomidate this pScan was made to be very modular so that additional packet types could easily be added, only needing a single file to be added and without changing any pre-existing code. 
The project pScan itself cannot process or return results from scans that it runs, this is why it is meant to be used with a passive inferincing tool which is capable of processing the packets and infering information from them. The point of pScan is soley to provide a simple to use API that can send less common packet types for researching into passive inferencing.

Python was used with this project because it is meant for testing at small scales, so we used a language which cold be quickly added too with additional packet types.
