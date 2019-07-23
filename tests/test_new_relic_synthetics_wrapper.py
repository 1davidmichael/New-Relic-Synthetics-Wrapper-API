import unittest
import responses
from new_relic_synthetics_wrapper import SyntheticsMonitor

class Testing(unittest.TestCase):

    @responses.activate
    def test_monitor_info(self):
        monitor = SyntheticsMonitor()
        path = f"https://synthetics.newrelic.com/synthetics/api/v3/monitors/example"

        responses.add(
            responses.GET,
            path,
            status=200,
            json={'error': 'not found'}
        )

        response = monitor.monitor_info('example')
        assert response['error'] == 'not found'

    @responses.activate
    def test_monitor_create(self):
        monitor = SyntheticsMonitor()
        path = f"https://synthetics.newrelic.com/synthetics/api/v3/monitors"

        responses.add(
            responses.POST,
            path,
            status=201,
            headers = {
                'location': 'https://synthetics.newrelic.com/accounts/2314308/monitors/fc9f2cc2-ee14-4a0b-85de-e7071dc31cdf'
            }
        )

        monitor_payload = {
            "name": "https://example.com",
            "type": "SIMPLE",
            "frequency": 1,
            "uri": "https://example.com",
            "locations": ["US_EAST_1"],
            "status": "ENABLED",
            "slaThreshold": 0.7,
            "options": {
                "validationString": "Test String",
                "verifySSL": True,
                "bypassHEADRequest": True,
                "treatRedirectAsFailure": True
            }
        }

        response = monitor.monitor_create(monitor_payload)
        response = 'https://synthetics.newrelic.com/accounts/2314308/monitors/fc9f2cc2-ee14-4a0b-85de-e7071dc31cdf'


    @responses.activate
    def test_monitor_id(self):
        monitor = SyntheticsMonitor()
        path = f"https://synthetics.newrelic.com/synthetics/api/v3/monitors"

        responses.add(
            responses.GET,
            path,
            status=200,
            json={
                "monitors": [
                    {
                        "id": "2a1bc369-7654-489d-918e-f6g135h7i2jk",
                        "name": "http://example.com",
                        "type": "BROWSER",
                        "frequency": 60,
                        "uri": "http://example.com",
                        "locations": [
                                "AWS_US_WEST_1"
                                        ],
                        "status": "DISABLED",
                        "slaThreshold": 7,
                        "options": {},
                        "modifiedAt": "2016-09-26T23:12:46.981+0000",
                        "createdAt": "2016-09-26T23:12:46.981+0000",
                        "userId": 0,
                        "apiVersion": "0.2.2"
                    }
                ],
                "count": 1
            }
        )

        response = monitor.get_monitor_id('http://example.com')
        assert response == '2a1bc369-7654-489d-918e-f6g135h7i2jk'

    @responses.activate
    def test_monitor_delete(self):
        monitor = SyntheticsMonitor()
        path = f"https://synthetics.newrelic.com/synthetics/api/v3/monitors/2a1bc369-7654-489d-918e-f6g135h7i2jk"

        responses.add(
            responses.DELETE,
            path,
            status=204,
        )

        response = monitor.monitor_delete('2a1bc369-7654-489d-918e-f6g135h7i2jk')
        assert response

    @responses.activate
    def test_monitor_update(self):
        monitor = SyntheticsMonitor()
        path = f"https://synthetics.newrelic.com/synthetics/api/v3/monitors/2a1bc369-7654-489d-918e-f6g135h7i2jk"
        monitor_payload = {
            "name": "https://example.com",
            "type": "SIMPLE",
            "frequency": 1,
            "uri": "https://example.com",
            "locations": ["US_EAST_1"],
            "status": "ENABLED",
            "slaThreshold": 0.7,
            "options": {
                "validationString": "Test String",
                "verifySSL": True,
                "bypassHEADRequest": True,
                "treatRedirectAsFailure": True
            }
        }

        responses.add(
            responses.PUT,
            path,
            status=204,
        )

        response = monitor.monitor_update('2a1bc369-7654-489d-918e-f6g135h7i2jk', monitor_payload)
        assert response

    @responses.activate
    def test_get_valid_locations(self):
        monitor = SyntheticsMonitor()
        path = "https://synthetics.newrelic.com/synthetics/api/v1/locations"

        responses.add(
            responses.GET,
            path,
            status=200,
            json={}
        )

        response = monitor.get_valid_locations()
        assert response == {}

if __name__ == '__main__':
    unittest.main()
