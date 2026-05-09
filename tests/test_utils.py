# Importing the functions to be tested, pytest and typing
import unittest
from unittest.mock import MagicMock, patch

from src.utils import get_transactions_dictionary


class TestCurrencyConversionAndJsonLoading(unittest.TestCase):
    """
        Unit test class for testing currency conversion and JSON loading functionalities.
    """

    @patch('builtins.open', new_callable=MagicMock)
    @patch('json.load')
    def test_get_transactions_dictionary(self, mock_json_load: MagicMock, mock_open: MagicMock) -> None:
        """
        Tests the get_transactions_dictionary function to ensure it correctly
        loads transaction data from a JSON file.
        """
        # Setting up a mock for json.load
        mock_open.return_value.__enter__.return_value = MagicMock()
        mock_json_load.return_value = [
            {'description': 'Транзакция 1', 'amount': 100, 'currency': 'USD'},
            {'description': 'Транзакция 2', 'amount': 200, 'currency': 'EUR'},
        ]

        # Call the function under test
        transactions = get_transactions_dictionary('operation.json')

        # Check that the transactions are loaded correctly
        self.assertEqual(len(transactions), 2)
        self.assertEqual(transactions[0]['description'], 'Транзакция 1')
        self.assertEqual(transactions[1]['amount'], 200)