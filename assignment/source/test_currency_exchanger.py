import unittest
from unittest.mock import patch, Mock
from currency_exchanger import CurrencyExchanger

class TestCurrencyExchanger(unittest.TestCase):

    @patch('requests.get')
    def test_currency_exchange(self, mock_get):
        # Mock response data
        mock_response = Mock()
        expected_response = {'base': 'THB', 'result': {'KRW': 38.69}}
        mock_response.json.return_value = expected_response
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        # Create an instance of the CurrencyExchanger
        exchanger = CurrencyExchanger(base_currency="THB", target_currency="KRW")

        # Test the currency exchange function
        amount_in_thb = 1000  # Amount in THB to be converted
        amount_in_krw = exchanger.currency_exchange(amount_in_thb)

        # Check if the conversion is correct
        self.assertEqual(amount_in_krw, 1000 * 38.69)

        # Ensure that the API was called with the correct parameters
        mock_get.assert_called_once_with("https://coc-kku-bank.com/foreign-exchange", params={'from': 'THB', 'to': 'KRW'})

if __name__ == '__main__':
    unittest.main()
