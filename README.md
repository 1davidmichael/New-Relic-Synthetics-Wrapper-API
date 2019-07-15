# New Relic Synthetics Wrapper

A wrapper around the [New Relic Synthetics API](https://docs.newrelic.com/docs/apis/synthetics-rest-api/monitor-examples/manage-synthetics-monitors-rest-api).

__Monitor Definition:__
```
{
"name": string [required],
"type": string (SIMPLE, BROWSER, SCRIPT_API, SCRIPT_BROWSER) [required],
"frequency": integer (minutes) [required, must be one of 1, 5, 10, 15, 30, 60, 360, 720, or 1440],
"uri": string [required for SIMPLE and BROWSER type],
"locations": array of strings [at least one required],
"status": string (ENABLED, MUTED, DISABLED) [required],
"slaThreshold": double,
"options": {
  "validationString": string [only valid for SIMPLE and BROWSER types],
  "verifySSL": boolean (true, false) [only valid for SIMPLE and BROWSER types],
  "bypassHEADRequest": boolean (true, false) [only valid for SIMPLE types],
  "treatRedirectAsFailure": boolean (true, false) [only valid for SIMPLE types]
  }
}
```

## Examples

### Create new monitor

Creating a monitor requires creating a monitor description object
and passing it into the `monitor_create` method.

```python
from new_relic_synthetics_wrapper import SyntheticsMonitor

monitor = SyntheticsMonitor()
monitor_payload = {
    "name": "https://www.google.com",
    "type": "SIMPLE",
    "frequency": 1,
    "uri": "https://www.google.com",
    "locations": [
        "AWS_US_EAST_1",
        "AWS_US_EAST_2",
        "AWS_US_WEST_1",
        "AWS_US_WEST_2",
        "LINODE_US_WEST_1",
        "LINODE_US_CENTRAL_1",
        "LINODE_US_EAST_1",
    ],
    "status": "ENABLED",
    "slaThreshold": 7.0,
    "options": {
        "validationString": "</html>",
        "verifySSL": True,
        "bypassHEADRequest": True,
        "treatRedirectAsFailure": True
    }
}

print(monitor.monitor_create(monitor_payload))
```

### Update monitor

Updating a monitor requires creating a monitor description object
and passing it into the `monitor_update` method.

```python
from new_relic_synthetics_wrapper import SyntheticsMonitor

monitor = SyntheticsMonitor()
monitor_payload = {
    "name": "https://www.google.com",
    "type": "SIMPLE",
    "frequency": 1,
    "uri": "https://www.google.com",
    "locations": [
        "AWS_US_EAST_1",
        "AWS_US_EAST_2",
        "AWS_US_WEST_1",
        "AWS_US_WEST_2",
        "LINODE_US_WEST_1",
        "LINODE_US_CENTRAL_1",
        "LINODE_US_EAST_1",
    ],
    "status": "ENABLED",
    "slaThreshold": 7.0,
    "options": {
        "validationString": "</html>",
        "verifySSL": True,
        "bypassHEADRequest": True,
        "treatRedirectAsFailure": True
    }
}

print(monitor.monitor_update(monitor_payload))
```

### Delete monitor

A monitor can be deleted by passing the monitor ID into the `monitor_delete`
method

```python
from new_relic_synthetics_wrapper import SyntheticsMonitor

monitor = SyntheticsMonitor()

monitor_id='a0809d5d-4c4e-46ab-b61e-66973d4521eb'

print(monitor.monitor_delete(monitor_id))
```
