from salut import salut
from unittest import mock

def my_input(*args, **kwargs):
    print("In functia mocked")
    return "Marcel"

@mock.patch('salut.input', my_input)
def test_salut():
    assert salut() == "Marcel"


def test_salut_manager():
    with mock.patch('salut.input', my_input) as mock_input:
        assert salut() == "Marcel"


def test_salut_manager_mock():
    with mock.patch('salut.input') as mock_input:
        mock_input.return_value = "Marcel"
        assert salut() == "Marcel"
        mock_input.assert_called_once()


