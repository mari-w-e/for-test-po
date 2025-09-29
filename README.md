# Отчет по Лабораторной работе №1

### Функции:
- add_product
- correct_date
- correct_price и is_number
- view_all_products
- view_products_by_date
- view_products_by_category
- sort_products_by_price
- delete_product
- save_to_file

### Критически важные участки:
- добавление и удаление товаров (так как происходит изменение списка товаров в файле)
- сортировка (по цене) и фильтрация (по дате и по категории) (так как нужно обеспечить корректный вывод данных пользователю)
- проверка корректности данных: дата, цена.

### Ключевые сценарии использоваия (use cases):
- добавление нового товара
- просмотр списка товаров
- сортировка по цене
- фильтрация по дате и по категории
- удаление товара

### Тесты
1. Тест для проверки корректной цены
   Тест проверяет работу программы при нормальном, корректном значении цены.
   arrange: присваиваем значение цене 123.45
   act: вызываем correct_price с этим значением
   assert: результат сравнивается с нужным 123.45

   ```python
   def test_correct_price_valid():
    # arrange
    price = "123.45"

    # act
    result = dz.correct_price(price)

    # assert
    assert result == 123.45
   ```
   
2. Тест для проверки цены при некорректном и корректном вводе
   Тест проверяет работу программы при некорректном вводе (строка вместо числа).
   arrange: cначала будет подаваться строка, затем корректное число
   act: вызываем correct_price
   assert: ожидавется результат числа, а не строки

   ```python
   def test_correct_price_invalid(monkeypatch):
    # arrange
    inputs = iter(["abc", "50"]) # некорректное и корректное значение
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    # act
    result = dz.correct_price("abc")

    # assert
    assert result == 50.0
   ```

3. Тест для проверки слишком большой цены
   Тест проверяет, что большая цена будет обрабатываться корректно и не будет записываться.
   arrange: сначала будет вводиться огромная цена, потом нормальная
   act: вызываем correct_price
   assert: ожидается результат корректной цены

   ```python
   def test_correct_price_out_of_range(monkeypatch):
    # arrange
    inputs = iter(["2000000", "100"]) # недопустимо большая цена и нормальная
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    # act
    result = dz.correct_price("20000")

    # assert
    assert result == 100.0
   ```

4. Тест для проверки корректной даты
   Тест проверяет работу программы при корректном значении даты.
   arrange: вводим корректное значение даты
   act: вызываем функцию test_correct_date
   assert: ожидаем корректный результат

   ```python
   def test_correct_date(): # если дата действительно корректная
    # arrange
    date = "02-12-2023"

    # act
    result = dz.correct_date(date)

    # assert
    assert result == "02-12-2023"
   ```
   
5. Тест для проверки некорректного формата
   Тест проверяет, что некоректный формат данных будет обработан и будет ожидаться корректный ввод.
   arrange: вводим сначала некорректные данные, потом корректный формат
   act: вызываем correct_date с первым некорректным форматом
   assert: ожидаем второе значение как корректное

   ```python
   def test_correct_date_invalid_format(monkeypatch):
    # arrange
    inputs = iter(["2023/12/02", "02-12-2023"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    # act
    result = dz.correct_date("изначально")

    # assert
    assert result == "02-12-2023"
   ```


6. Тест для проверки сотрировки по дате
   Тест проверяет верное отображение при сортировке товаров по цене.
   arrange: подаем два товара, у одого цена меньше, у другого - больше; имитируем ввод 1 (т.к. сортировка по возрастанию)
   act: вызываем sort_products_by_price
   assert: проверяем, что первый товар - с наименьшей ценой

   ```python
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

   ```

13. Тест для проверки удаления товара
   Тест проверяет, что при удалении товара он действительно будет удален из списка товаров
   arrange: изначально говорим, что в списке товаров есть один товар, выбираем его для удаления
   act: вызываем delete_product
   assert: ожидаем, что список товаров станет пустым и выведется сообщение о том, что товар успешно удален
   ```python
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
   ```

### Результаты тестов

При запуске локально были получены следующие результаты:
```
============================= test session starts =============================
collecting ... collected 7 items

test_dz.py::test_correct_price_valid PASSED                              [ 14%]
test_dz.py::test_correct_price_invalid PASSED                            [ 28%]
test_dz.py::test_correct_price_out_of_range PASSED                       [ 42%]
test_dz.py::test_correct_date_valid PASSED                               [ 57%]
test_dz.py::test_correct_date_invalid_format PASSED                      [ 71%]
test_dz.py::test_sort_products_by_price PASSED                           [ 85%]
test_dz.py::test_delete_product PASSED                                   [100%]

============================== 7 passed in 0.07s ==============================
```

С помощью github actions были получены следующие результаты покрытия кода:

```
Run pytest --cov=dz --cov-report=xml --cov-report=term-missing
============================= test session starts ==============================
platform linux -- Python 3.12.11, pytest-8.4.2, pluggy-1.6.0
rootdir: /home/runner/work/for-test-po/for-test-po
plugins: cov-7.0.0
collected 7 items

test_dz.py .......                                                       [100%]

================================ tests coverage ================================
_______________ coverage: platform linux, python 3.12.11-final-0 _______________

Name    Stmts   Miss  Cover   Missing
-------------------------------------
dz.py     151     89    41%   10-20, 35-49, 53-60, 66, 86, 96-101, 107-122, 128-144, 152, 155-156, 172, 190-191, 195-222
-------------------------------------
TOTAL     151     89    41%
Coverage XML written to file coverage.xml
============================== 7 passed in 0.30s ===============================
```

По результатам можно сделать следующие выводы.

Все 7 тестов прошли успешно.

Покрытие кода - 41%. Всего было 151 строка, 89 из них не были покрыты тестами.

Покрытие кода низкое, но здесь достаточно примитивный проект, например меню тут тестироваться не может. 

Покрытие кода можно увеличить, если прописать больше тестов на добавление, просмотр товаров. Можно рассмотреть больше вариантов некорретного ввода пользователем.

Тесты построены по принципу AAA. Также соответсвуют принципу FIRST (быстрота, изолированность, воспроизводимость, самопроверяемость, своевременность).

Показатель покрытия кода, действительно низкий, но это объясняется тем, что эти строки в большинстве относятся к меню или функциям просмотра.


   
   
