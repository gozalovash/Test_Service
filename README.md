#  Text Service application using TCP

This project is designed to boost the network programming knowledge by solving different labs

## Prerequisites

- Python3
- OOP understanding


## Libraries used

```python
import socket
import argparse
import json
import os
```
## Content
- Server.py - Server part of programm, which performs operations, requested by client
- Client.py - Client part, send request to Server to perform specific operation and necessary files
- my_source_file  - source file with the original text
- my_key - the key for encoding/decoding
- my_json_file.json - dictionary with values for changing the text
- response - the response from the server is written here
 #### Scenario
 > You as a software developer must create the client-server-based console app “text_service”.
With the next abilities:
- Change text: The sender sends the text file to the server and the json file, in respond the server
must read the json file and swap the words from the text according the json file.
- Encode/Decode text: The sender sends the text file and the key (another text) on the respond
the server must XOR the text message with the key (One Time Pad cipher) and return it to the
client. The decoding process happens in the same way where instead of the text message the
client sends 

   #### Task
 >Create console based app with the options (modes) with to swap and encode/decode text
python3 text_service --mode chance_text my_source_file my_json_file.json
python3 text_service --mode encode_decode my_source_file my_key


## Usage

First run the program as server:

```
python Server.py
```
Then as a client, providing necessary arguments:

```
python Client.py [--mode MODE] {source_file} {key_file}
```
Example:
```
python Client.py --mode change_text my_source_file my_json_file.json
```


