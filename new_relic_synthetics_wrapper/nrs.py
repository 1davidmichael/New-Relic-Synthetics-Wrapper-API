from . import session

class SyntheticsMonitor(object):
    def __init__(self):
        pass

    def monitor_info(self, id):
        self.id = id
        path = f"https://synthetics.newrelic.com/synthetics/api/v3/monitors/{self.id}"
        response = session.get(path)
        return response.json()

    def monitor_create(self, monitor_payload):
        path = f"https://synthetics.newrelic.com/synthetics/api/v3/monitors"
        session.headers['content-type'] = 'application/json'
        response = session.post(path, json=monitor_payload)

        if response.status_code == 201:
            return response.headers['location']

    def monitor_delete(self, id):
        self.id = id
        path = f"https://synthetics.newrelic.com/synthetics/api/v3/monitors/{self.id}"
        response = session.delete(path)
        if response.status_code == 204:
            return True

    def get_monitor_id(self, name):
        self.name = name
        path = f"https://synthetics.newrelic.com/synthetics/api/v3/monitors"
        response = session.get(path)
        for monitor in response.json()['monitors']:
            if monitor['name'] == self.name:
                return monitor['id']

    def monitor_update(self, id, monitor_payload):
        self.id = id
        path = f"https://synthetics.newrelic.com/synthetics/api/v3/monitors/{self.id}"
        session.headers['content-type'] = 'application/json'
        response = session.put(path, json=monitor_payload)

        if response.status_code == 204:
            return True

    def get_valid_locations(self):
        path = "https://synthetics.newrelic.com/synthetics/api/v1/locations"
        response = session.get(path)
        return response.json()
