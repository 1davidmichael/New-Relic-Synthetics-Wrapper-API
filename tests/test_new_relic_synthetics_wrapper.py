import unittest
from unittest.mock import Mock

from new_relic_synthetics_wrapper import SyntheticsMonitor

class Testing(unittest.TestCase):
    def test_monitor_info(self):
        """Tests an API call to get a monitor info"""

        monitor = SyntheticsMonitor()
        response = monitor.info('fc9f2cc2-ee14-4a0b-85de-e7071dc31cdf')

        self.assertTrue(isinstance(response, dict))
        self.assertEqual(response['id'], 'fc9f2cc2-ee14-4a0b-85de-e7071dc31cdf')

if __name__ == '__main__':
    unittest.main()

# def test_monitor_create():
