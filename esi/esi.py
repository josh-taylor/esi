import requests


class User:
    pass


class Device:
    pass


class Esi:
    def __init__(self):
        self.url = "https://esiheating.uksouth.cloudapp.azure.com/centro"
        self.token = None
        self.user_id = None

    def login(self, username, password):
        """Attempt a login with a username and password. Returns user details on success."""
        payload = {
            'email': username,
            'password': password,
            'password_encryption': 'password_encryption'
        }

        r = requests.post(f"{self.url}/login", data=payload)
        r = r.json()

        user = User()
        user.token = r['user']['token']
        user.id = r['user']['id']

        return user

    def authenticate(self, token, user_id):
        """Authenticate the client with the given token and user_id. Usually retrieved from login()"""
        self.token = token
        self.user_id = user_id

    def get_device_list(self, device_type=['02', '04', '10', '20', '23', '25']):
        """Fetch a list of devices associated with the authenticated account"""

        payload = {
            'token': self.token,
            'user_id': self.user_id,
            'device_type': ','.join(device_type)
        }

        # TODO handle the login page when unauthenticated
        r = requests.post(f"{self.url}/getDeviceList", data=payload)
        r = r.json()

        devices = []

        for d in r['devices']:
            device = Device()
            device.id = d['device_id']
            device.name = d['device_name']
            device.current_temperature = d['current_temprature']
            device.inside_temperature = d['inside_temparature']
            devices.append(device)

        return devices

    def set_thermostat(self, device_id, current_temperature, work_mode=5, message_id="1111"):
        """Set the current temperature of a thermostat"""

        payload = {
            'token': self.token,
            'user_id': self.user_id,
            'device_id': device_id,
            'current_temprature': current_temperature,
            'work_mode': work_mode,
            'messageId': message_id,
        }

        r = requests.post(f"{self.url}/setThermostatWorkModeNew", data=payload)

        return r
