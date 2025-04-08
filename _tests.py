import pytest
from rich-test import run_tasks

def test_run_tasks():
    try:
        run_tasks()
    except Exception as e:
        pytest.fail(f"run_tasks raised an exception: {e}")
