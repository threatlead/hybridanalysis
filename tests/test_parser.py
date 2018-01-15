from .context import hybridanalysis
from ..settings import API_SECRET, API_KEY
import unittest


class ConnectTestSuite(unittest.TestCase):

    def test_ha_key_data(self):
        response = hybridanalysis.HybridAnalysis(api_key=API_KEY, api_secret=API_SECRET).api_key_data()
        self.assertEqual(response['response'], 0, 'Invalid Response for key_data check.')

    def test_ha_quota(self):
        response = hybridanalysis.HybridAnalysis(api_key=API_KEY, api_secret=API_SECRET).quota()
        self.assertEqual(response['response'], 0, 'Invalid Response for quota check.')

    def test_ha_feed(self):
        response = hybridanalysis.HybridAnalysis(api_key=API_KEY, api_secret=API_SECRET).feed(days=1)
        self.assertEqual(response['response'], 0, 'Invalid Response for feed check.')

    def test_ha_limits(self):
        response = hybridanalysis.HybridAnalysis(api_key=API_KEY, api_secret=API_SECRET).limits()
        self.assertEqual(response['response'], 0, 'Invalid Response for feed check.')

    def test_ha_environments(self):
        response = hybridanalysis.HybridAnalysis(api_key=API_KEY, api_secret=API_SECRET).environments()
        self.assertEqual(response['response'], 0, 'Invalid Response for feed check.')

    def test_ha_scan(self):
        sha256 = '040c0111aef474d8b7bfa9a7caa0e06b4f1049c7ae8c66611a53fc2599f0b90f'
        response = hybridanalysis.HybridAnalysis(api_key=API_KEY, api_secret=API_SECRET).scan(sha256=sha256)
        self.assertEqual(response['response'], 0, 'Invalid Response for scan check.')


if __name__ == '__main__':
    unittest.main()
