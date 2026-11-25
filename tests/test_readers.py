from unittest.mock import patch

import pandas as pd
import pytest

from src.readers import read_csv_transactions, read_excel_transactions


@patch('src.readers.pd.read_csv')
def test_read_csv_transactions_success(mock_read_csv):
    """Тест: успешное чтение CSV-файла."""
    fake_df = pd.DataFrame([
        {"id": 1, "amount": 100.0, "currency": "RUB"},
        {"id": 2, "amount": 250.5, "currency": "USD"}
    ])
    mock_read_csv.return_value = fake_df
    result = read_csv_transactions("fake_path.csv")
    assert result == [
        {"id": 1, "amount": 100.0, "currency": "RUB"},
        {"id": 2, "amount": 250.5, "currency": "USD"}
    ]
    mock_read_csv.assert_called_once_with("fake_path.csv")


@patch('src.readers.pd.read_csv')
def test_read_csv_transactions_empty(mock_read_csv):
    """Тест: CSV-файл пуст (нет данных)."""
    mock_read_csv.return_value = pd.DataFrame()
    result = read_csv_transactions("empty.csv")
    assert result == []


@patch('src.readers.pd.read_csv')
def test_read_csv_transactions_not_found(mock_read_csv):
    """Тест: CSV-файл не найден."""
    mock_read_csv.side_effect = FileNotFoundError
    result = read_csv_transactions("missing.csv")
    assert result == []


@patch('src.readers.pd.read_csv')
def test_read_csv_transactions_empty_data_error(mock_read_csv):
    """Тест: CSV-файл пуст (вызывает EmptyDataError)."""
    mock_read_csv.side_effect = pd.errors.EmptyDataError
    result = read_csv_transactions("empty.csv")
    assert result == []


@patch('src.readers.pd.read_excel')
def test_read_excel_transactions_success(mock_read_excel):
    """Тест: успешное чтение Excel-файла."""
    fake_df = pd.DataFrame([
        {"id": 1, "amount": 100.0, "currency": "RUB"},
        {"id": 2, "amount": 250.5, "currency": "USD"}
    ])
    mock_read_excel.return_value = fake_df
    result = read_excel_transactions("fake_path.xlsx")
    assert result == [
        {"id": 1, "amount": 100.0, "currency": "RUB"},
        {"id": 2, "amount": 250.5, "currency": "USD"}
    ]
    mock_read_excel.assert_called_once_with("fake_path.xlsx")


@patch('src.readers.pd.read_excel')
def test_read_excel_transactions_empty(mock_read_excel):
    """Тест: Excel-файл пуст."""
    mock_read_excel.return_value = pd.DataFrame()
    result = read_excel_transactions("empty.xlsx")
    assert result == []


@patch('src.readers.pd.read_excel')
def test_read_excel_transactions_not_found(mock_read_excel):
    """Тест: Excel-файл не найден."""
    mock_read_excel.side_effect = FileNotFoundError
    result = read_excel_transactions("missing.xlsx")
    assert result == []
