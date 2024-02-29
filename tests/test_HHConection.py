import pytest
from src.hh_conection import GetHadHanter

@pytest.fixture
def get_head_hunter():
    return GetHadHanter("python", 1)


def test_str(get_head_hunter):
    """
    Проверка метода str
    """
    assert str(get_head_hunter) == "python"

def test_repr(get_head_hunter):
    """
    Проверка метода repr
    """
    assert repr(get_head_hunter) == 'GetHadHanter(python, 1)'

def test_url(get_head_hunter):
    """
    Проверка работоспособности ссылки
    """
    assert get_head_hunter.url == "https://api.hh.ru"



def test_error_connection():
    """
    Проверка на наличие ошибок
    """
    with pytest.raises(TypeError):
        GetHadHanter()
