import os
import requests

NR_ADMIN_USER_KEY = os.environ.get('NR_ADMIN_USER_KEY', None)

class APIKeyMissingError(Exception):
    pass

if NR_ADMIN_USER_KEY is None:
    raise APIKeyMissingError(
        "All methods require an API key. See:"
        "https://docs.newrelic.com/docs/apis/synthetics-rest-api/monitor-examples/manage-synthetics-monitors-rest-api"
    )

session = requests.Session()
session.headers = {}
session.headers['x-api-key'] = NR_ADMIN_USER_KEY

from .nrs import SyntheticsMonitor
