# pyesi

## Introduction

Python API to the ESI API for monitoring and controlling your thermostat.

## Usage

**Authenticate**

You need to log in and authenticate the client.

```python
from esi import *

client = Esi()
user = client.login()
client.authenticate(user.token, user.user_id)
```

**Get device list**

You can discover all of your devices

```python
devices = client.get_device_list()
for device in devices:
    print(
        f"Name: {device.name}, Temp: {device.inside_temperature} ({device.current_temperature})")
```

**Set thermostat**

You can update the current temperature

```python
client.set_thermostat(device.id, "180")
```
