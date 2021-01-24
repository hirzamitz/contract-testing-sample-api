import atexit
import unittest
from consumer_app import get_item

from pact import Consumer, Provider

pact = Consumer('consumer_app').has_pact_with(Provider('provider_app'), port=5000)
pact.start_service()
atexit.register(pact.stop_service)
class GetItemContract(unittest.TestCase):
  def test_get_item(self):
    expected = {
      'name': 'Strawberries',
      'id': 1,
      'count': 2,
    }
    (pact
     .given('Item exists')
     .upon_receiving('a request for id 1')
     .with_request('get', '/provider/api/items/1')
     .will_respond_with(200, body=expected))
    with pact:
      result = get_item('1')
    self.assertEqual(result, expected)