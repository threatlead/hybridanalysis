import requests
from requests.auth import HTTPBasicAuth


class HybridAnalysis:
    """
    HybridAnalysis : Ingest site data
    """
    base_url = 'https://www.hybrid-analysis.com'
    user_agent = 'VxApi CLI Connector'

    def __init__(self, api_key, api_secret):
        self.session = requests.Session()
        self.session.headers.update({'User-Agent': HybridAnalysis.user_agent})
        self.session.auth = HTTPBasicAuth(api_key, api_secret)
        self.auth_level = None
        self.auth_level_name = None
        self.api_key_data()

    def api_key_data(self, ):
        endpoint = '/'.join([HybridAnalysis.base_url, 'api/get-api-key-data'])
        response = self.session.get(url=endpoint)
        if not response.status_code == 200:
            return False
        self.auth_level = response.json()['response']['auth_level']
        self.auth_level_name = response.json()['response']['auth_level_name']
        return response.json()

    def quota(self, ):
        endpoint = '/'.join([HybridAnalysis.base_url, 'api/quota'])
        response = self.session.get(url=endpoint)
        if not response.status_code == 200:
            return False
        return response.json()

    def limits(self, ):
        endpoint = '/'.join([HybridAnalysis.base_url, 'api/api-limits'])
        response = self.session.get(url=endpoint)
        if not response.status_code == 200:
            return False
        return response.json()

    def environments(self, ):
        endpoint = '/'.join([HybridAnalysis.base_url, 'api/environments'])
        response = self.session.get(url=endpoint)
        if not response.status_code == 200:
            return False
        return response.json()

    def feed(self, days=1):
        endpoint = '/'.join([HybridAnalysis.base_url, 'api/feed/{0}'.format(days)])
        response = self.session.get(url=endpoint)
        if not response.status_code == 200:
            return False
        return response.json()

    def result(self, sha256):
        if not self.auth_level_name == 'default':
            return 'Result API cannot be used due to privileges'
        endpoint = '/'.join([HybridAnalysis.base_url, 'api/result/{0}'.format(sha256)])
        response = self.session.get(url=endpoint)
        if not response.status_code == 200:
            return False
        return response.json()

    def scan(self, sha256):
        endpoint = '/'.join([HybridAnalysis.base_url, 'api/scan/{0}'.format(sha256)])
        response = self.session.get(url=endpoint)
        if not response.status_code == 200:
            return False
        return response.json()
