# Importing the functions to be tested, pytest and typing
import unittest
from typing import Any, Dict
from unittest.mock import Mock, patch

from src.external_api import convert_currency_to_rub


class TestConvertCurrencyToRub(unittest.TestCase):
    """
    Unit test class for the convert_currency_to_rub function.
    """

    @patch('src.external_api.requests.request')
    def test_convert_currency_to_rub_success(self, mock_request: Mock) -> None:
        """
        Tests the successful conversion of currencies to RUB.
        """
        # Mock the response from the API
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'rates': {
                'USD': 0.015,
                'EUR': 0.013
            }
        }
        mock_request.return_value = mock_response

        # Create a mock transaction
        transaction_usd: Dict[str, Any] = {
            'operationAmount': {
                'amount': '100',
                'currency': {'code': 'USD'}
            }
        }

        transaction_eur: Dict[str, Any] = {
            'operationAmount': {
                'amount': '100',
                'currency': {'code': 'EUR'}
            }
        }

        expected_usd_to_rub = 100 * (1/0.015)
        expected_eur_to_rub = 100 * (1/0.013)

        # Assert the conversion results
        self.assertAlmostEqual(convert_currency_to_rub(transaction_usd), expected_usd_to_rub)
        self.assertAlmostEqual(convert_currency_to_rub(transaction_eur), expected_eur_to_rub)

    @patch('src.external_api.requests.request')
    def test_convert_currency_to_rub_rate_not_found(self, mock_request: Mock) -> None:
        """
        Tests the conversion when the currency rate is not found.
        """
        # Mock the response without the specific rate
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'rates': {}
        }
        mock_request.return_value = mock_response

        transaction: Dict[str, Any] = {
            'operationAmount': {
                'amount': '100',
                'currency': {'code': 'GBP'}
            }
        }

        # Assert that conversion is 0.0 when rate is not found
        self.assertEqual(convert_currency_to_rub(transaction), 0.0)

    @patch('src.external_api.requests.request')
    def test_convert_currency_to_rub_api_error(self, mock_request: Mock) -> None:
        """
        Tests the conversion when the API returns an error.
        """
        # Mock a failed API response
        mock_response = Mock()
        mock_response.status_code = 500
        mock_request.return_value = mock_response

        transaction: Dict[str, Any] = {
            'operationAmount': {
                'amount': '100',
                'currency': {'code': 'USD'}
            }
        }

        # Assert that conversion is 0.0 on API error
        self.assertEqual(convert_currency_to_rub(transaction), 0.0)

    def test_convert_currency_to_rub_missing_data(self) -> None:
        """
        Tests the conversion when required data is missing from the transaction.
        """
        transaction: Dict[str, Any] = {
            # Missing 'operationAmount'
        }

        # Assert that conversion is 0.0 when data is missing
        self.assertEqual(convert_currency_to_rub(transaction), 0.0)