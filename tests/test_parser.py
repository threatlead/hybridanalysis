from .context import hybridanalysis
from ..settings import API_SECRET, API_KEY
import unittest


class ConnectTestSuite(unittest.TestCase):

    def setUp(self):
        self._connection = hybridanalysis.HybridAnalysis(api_key=API_KEY, api_secret=API_SECRET)

    def test_ha_key_data(self):
        response = self._connection.api_key_data()
        self.assertEqual(response['response_code'], 0, 'Invalid Response for key_data check.')

    def test_ha_quota(self):
        response = self._connection.quota()
        self.assertEqual(response['response_code'], 0, 'Invalid Response for quota check.')

    def test_ha_feed(self):
        response = self._connection.feed(days=1)
        self.assertEqual(response['status'], 'ok', 'Invalid Response for feed check.')

    def test_ha_limits(self):
        response = self._connection.limits()
        self.assertEqual(response['response_code'], 0, 'Invalid Response for feed check.')

    def test_ha_environments(self):
        response = self._connection.environments()
        self.assertEqual(response['response_code'], 0, 'Invalid Response for feed check.')

    def test_ha_scan(self):
        sha256 = '040c0111aef474d8b7bfa9a7caa0e06b4f1049c7ae8c66611a53fc2599f0b90f'
        response = self._connection.scan(sha256=sha256)
        self.assertEqual(response['response_code'], 0, 'Invalid Response for scan check.')


if __name__ == '__main__':
    unittest.main()
