import pytest
from sympy import python

import dz


# Тесты для correct_price
def test_correct_price_valid():
    # arrange
    price = "123.45"

    # act
    result = dz.correct_price(price)

    # assert
    assert result == 123.45

def test_correct_price_invalid(monkeypatch):
    # arrange
    inputs = iter(["abc", "50"]) # некорректное и корректное значение
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    # act
    result = dz.correct_price("abc")

    # assert
    assert result == 50.0


def test_correct_price_out_of_range(monkeypatch):
    # arrange
    inputs = iter(["2000000", "100"]) # недопустимо большая цена и нормальная
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    # act
    result = dz.correct_price("20000")

    # assert
    assert result == 100.0


# Тесты для correct_date
def test_correct_date(): # если дата действительно корректная
    # arrange
    date = "02-12-2023"

    # act
    result = dz.correct_date(date)

    # assert
    assert result == "02-12-2023"

def test_correct_date_invalid_format(monkeypatch):
    # arrange
    inputs = iter(["2023/12/02", "02-12-2023"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    # act
    result = dz.correct_date("изначально")

    # assert
    assert result == "02-12-2023"


# Тест для сортировки
def test_sort_products_by_price(monkeypatch, capsys):
    # arrange
    dz.products = [
        {"category": "cat", "name": "a", "price": 200, "date": "01-01-2022"},
        {"category": "cat", "name": "b", "price": 100, "date": "01-01-2022"},
    ]
    monkeypatch.setattr("builtins.input", lambda _: "1") # сортировка по возрастанию (вводим 1)

    # act
    dz.sort_products_by_price()

    # asssert
    captured = capsys.readouterr()
    assert "b" in captured.out.splitlines()[3] # берем 4 строку, т.к. первые 3 - шапка
    # проверяем, что первый сверху товар - b


# Тест для удаления
def test_delete_product(monkeypatch, capsys):
    # arrange
    dz.products = [
        {"category": "cat", "name": "a", "price": 200, "date": "01-01-2022"},
    ]
    monkeypatch.setattr("builtins.input", lambda _: "a") # ввод товара a для удаления

    # act
    dz.delete_product()

    # asssert
    assert dz.products == []
    captured = capsys.readouterr()
    assert "Товар успешно удален." in captured.out
