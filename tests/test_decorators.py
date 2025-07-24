from decorators import log
import pytest
import datetime
import functools
from typing import Optional, Callable
from unittest.mock import patch, mock_open
from pathlib import Path


def test_log_decorator_without_file(capsys: pytest.CaptureFixture[str]) -> None:
    """Проверяем вывод в консоль при отсутствии файла для логирования."""

    @log()
    def dummy_func(a: int, b: int) -> int:
        return a + b

    result = dummy_func(2, 3)
    captured = capsys.readouterr()

    assert result == 5
    assert "dummy_func ok. Inputs: (2, 3), {}." in captured.out
    assert "Start time:" in captured.out
    assert "End time:" in captured.out


def test_log_decorator_with_exception(capsys: pytest.CaptureFixture[str]) -> None:
    """Проверяем вывод ошибки в консоль."""

    @log()
    def error_func() -> None:
        raise ValueError("Test error")

    with pytest.raises(ValueError, match="Test error"):
        error_func()

    captured = capsys.readouterr()
    assert "error_func error: Test error" in captured.out
    assert "Start time:" in captured.out
    assert "End time:" in captured.out


def test_log_decorator_with_file(tmp_path: Path) -> None:
    """Проверяем запись в файл."""
    test_file = tmp_path / "test_log.txt"

    @log(str(test_file))
    def dummy_func(a: int, b: int) -> int:
        return a + b

    result = dummy_func(2, 3)

    assert result == 5
    assert test_file.exists()

    content = test_file.read_text()
    assert "dummy_func ok. Inputs: (2, 3), {}." in content
    assert "Start time:" in content
    assert "End time:" in content


def test_log_decorator_timestamps() -> None:
    """Проверяем временные метки с моком datetime."""
    test_time = datetime.datetime(2023, 1, 1, 12, 0, 0)

    with patch("datetime.datetime") as mocked_datetime:
        mocked_datetime.now.return_value = test_time

        @log()
        def timed_func() -> int:
            return 42

        with patch("builtins.print") as mocked_print:
            timed_func()
            mocked_print.assert_called_once()
            log_message = mocked_print.call_args[0][0]
            assert f"Start time: {test_time}, End time: {test_time}" in log_message


def test_log_decorator_preserves_function_metadata() -> None:
    """Проверяем сохранение метаданных функции."""

    @log()
    def func_with_metadata(a: int, b: int) -> int:
        """Test function"""
        return a + b

    assert func_with_metadata.__name__ == "func_with_metadata"
    assert func_with_metadata.__doc__ == "Test function"
    assert func_with_metadata.__annotations__ == {"a": int, "b": int, "return": int}


def test_log_decorator_with_kwargs(tmp_path: Path) -> None:
    """Проверяем обработку kwargs."""
    test_file = tmp_path / "test_log.txt"

    @log(str(test_file))
    def kwargs_func(a: int, b: int = 0) -> int:
        return a + b

    result = kwargs_func(2, b=3)

    assert result == 5
    assert test_file.exists()

    content = test_file.read_text()
    assert "kwargs_func ok. Inputs: (2,), {'b': 3}." in content
