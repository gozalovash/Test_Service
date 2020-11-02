# Network Programming

This project is designed to boost the network programming knowledge by solving different labs

## Prerequisites

- Python3
- OOP understanding


## Libraries used

```python
import socket
import argparse
from datetime import datetime
import random
```
## Content
- lab1_spotify.py- first lab

 #### Scenario
 > The Spotify regional server warehouse provides music streaming services for the billions of clients 24/7. Spotify servers responding time are depend on clients load number. Because of this reason, the clients must wait for responding with regarding the next time schedule: 
- First interval: Between 12:00 – 17:00 the maximum wait time must be 2 seconds.
- Second Interval: After the 17:00 till the 23:59 the maximum wait time must be for 4 seconds. 
- Third Interval: After the 23:59 till the 12:00 of the next day the waiting time must be 1 second 

> The exponential backoff of these intervals must be increased by the next factors: For the first and third intervals: doubles each iteration For the second interval: triples on each iteration 
   #### Task
 > Create the Client-Server based UDP basic console application with simple test messaging from the client to the server but with the backoff strategies based on the scenario above.

## Usage

To run the program as server:

```
python lab1_spotify.py server [HOST] [PORT]
```
To run as client:

```
python lab1_spotify.py client [HOST] [PORT]
```


