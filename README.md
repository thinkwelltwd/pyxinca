# pyXinca

This is a python library for communicating with ZuluDesk and Xinca MDM via their
REST API.

The API has various endpoints and not all of them are implemented with functions.
However the library has `http_get`, `http_post` and `http_delete` functions that
accept arbitrary URLs.

Consult the [Xinca / ZuluDesk REST API documentation](https://apiv6.xincamdm.com/docs/#api-_)
 for comprehensive requirements for using their REST API.

## Install

Install by cloning the repo and run `setup.py`.

```bash
$ python3 setup.py install
```

## Add an API user

You have to create an API user in Xinca / ZuluDesk to use the API. In the Xinca / ZuluDesk
console, go to Organization / Settings / API.

1. Check to Enable the API
2. Create an API key
3. Note the username automatically provided

## Usage

To initialize do the following.

```python
from pyxinca import Xinca
xinca = Xinca('apiuser', 'mypassword', 'https://apiv6.xincamdm.com')
```

Here are some examples on what you can do with the generic built-in functions.

```python
xinca.http_get(url, params=params)
xinca.http_post(url, data=data)
xinca.http_delete(url)

```

The library support wrappers for Apps, DEP, Devices, Groups, Profiles, and Users.

```python
# List of Apps
xinca.apps.list()

# Overview of DEP devices
xinca.dep.list()

# List of Devices
xinca.devices.list()

# Get device details by UDID number
xinca.devices.get(udid):

# To include installed apps, add the `includeApps` parameter.
xinca.devices.get(udid, params={'includeApps': True}):

# List of Groups
xinca.groups.list()

# List of Profiles
xinca.profiles.list()

# Get details about a Profile
xinca.profiles.get(profile_id)

# List of Users
xinca.users.list()

# List of iBeacons
xinca.ibeacons.list()
```
