## Инструкция к проекту по тестированию API микросервиса

Цель данного проекта - разработка набора автоматизированных тестов для тестирования API микросервиса. Тесты написаны на Python с использованием библиотеки `pytest`. Результатом проекта станет набор автоматизированных тестов, покрывающих основные сценарии использования API микросервиса.

### Основные задачи проекта

**Проверка корректности работы различных эндпоинтов API микросервиса**
- Проверка возвращаемых HTTP-кодов ответов
- Проверка структуры и содержимого ответов в формате JSON

**Тестирование различных сценариев использования API**
- Проверка работы API при передаче корректных данных
- Проверка работы API при передаче некорректных данных
- Проверка работы API при выполнении CRUD-операций (Create, Read, Update, Delete)

**Обеспечение стабильности и надежности API микросервиса**
- Выявление и устранение ошибок и уязвимостей в API
- Обеспечение соответствия API спецификациям и требованиям

**Повышение качества разработки и поддержки API микросервиса**
- Автоматизация процесса тестирования API

### Структура проекта

- [test_api](/test_api.py) — основной файл, содержащий тесты для тестирования API.
- [TESTCASES.md](/TESTCASES.md) — файл описания тест-кейсов.
- [BUGS.md](/BUGS.md) — файл с баг-репортами для обнаруженных ошибок в API микросервиса.

### Порядок подготовки к запуску тестов (описан порядок для Windows)

1. Клонируйте репозиторий.

        git clone https://github.com/kulaevvs/avito.tech.git

2. Перейдите в директорию проекта.

        cd repository

3. Создайте виртуальное окружение.

        python -m venv venv
   
5. Активируйте виртуальное окружение.

        venv\Scripts\activate

### Запуск тестов

Для запуска тестов используйте следующую команду.

        pytest

При запуске тестового сценария вывод в консоли будет содержать информацию о прохождении или падении тестов, а также подробные сообщения об ошибках, если таковые возникнут.

Команда запуска тестов может выполняться с различными ключами, например:

        pytest -v

Запуск тестов с включенным режимом подробного вывода (verbose mode). Это позволяет получить более подробную информацию о ходе выполнения тестов.
        
        pytest -l

Запуск тестов с включенным режимом вывода информации о локальных переменных (local variables). Когда вы запускаете тесты с этим флагом, pytest будет выводить значения локальных переменных в месте, где произошла ошибка или неудачное завершение теста. Это может быть очень полезно при отладке, когда вы хотите понять, какие значения имели переменные в момент возникновения ошибки.

### Описание проводимых тестов при тестировании API

**Тест 1. Наименование: test_post_announce.**
Выполняет тестовое создание объявления, содержащего валидные данные. Ожидаемый результат: успешное создание объявления и возврат статус кода 200 OK.

**Тест 2. Наименование: test_get_announce_by_id.**
Выполняет тестовое получение объявления по его существующему ID. Ожидаемый результат: успешное получение объявления и его данных.

**Тест 3. Наименование: test_get_all_announce_by_seller.**
Выполняет тестовое получение всех объявлений, связанных с ID продавца. Дополнительно генерирует три объявления с указанным ID. Ожидаемый результат: проверка количества полученных объявлений для указанного ID продавца. Прохождение теста, если их количество более трёх.

**Тест 4. Наименование: test_post_announce_error_data.**
Выполняет тестовое создание объявления с некорректными данными (без поля 'price'). Ожидаемый результат: возврат ошибки валидации со статус кодом 400 Bad Request.

**Тест 5. Наименование: test_get_announce_error_id.**
Выполняет тестовое получение объявления с несуществующим ID. Ожидаемый результат: возврат ошибки со статусом 404 Not Found.

### Настройка переменных для выполнения тестов

В процессе выполнения тестирования API, для корректной работы тестов, задаются следующие переменные:

`test_base_URL = "https://qa-internship.avito.com/api/1"`

`test_seller_ID = 987531`

`test_error_ID = "09209618-5494-488e-89f3-966366b361a7_35"`

```
test_payload = {
    "name": "Nokia",
    "price": 12500,
    "sellerId": test_seller_ID,
    "statistics": {
        "contacts": 25,
        "likes": 15,
        "viewCount": 17
    }
}
```
```
test_error_payload = {
    "name": "Nokia",
    "sellerId": test_seller_ID,
    "statistics": {
        "contacts": 25,
        "likes": 15,
        "viewCount": 17
    }
}
```

**Пояснения по используемым переменным:**
- test_base_URL - базовый URL API,
- test_seller_ID - идентификатор продавца,
- test_error_ID - ошибочный идентификатор товара,
- test_payload - полезная нагрузка, содержит данные для тестового создания объявления,
- test_error_payload - полезная нагрузка, содержит ошибочные данные для тестового создания объявления.

### Примеры выполнения тестов API

#### Тестовое создание объявления

```
# Выполняем тест на создание объявления
def test_post_announce():
    """Тест на создание объявления"""
    url = f"{test_base_URL}/item"
    response = requests.post(url, json=test_payload, timeout=5)
    assert response.status_code == 200
    json_response = response.json()
    assert "id" in json_response

json_response = {'status': 'Сохранили объявление - 040bcfb9-5162-4611-b29d-61127fb32fa6'}
response   = <Response [200]>
url        = 'https://qa-internship.avito.com/api/1/item'
```

#### Тестовое получение объявления

```
# Выполняем тест на получение объявления по его ID
def test_get_announce_by_id(create_announce):
    """Тест на получение объявления по ID"""
    get_url = f"{test_base_URL}/item/{create_announce}"
    get_response = requests.get(get_url, timeout=5)
    assert get_response.status_code == 200
    json_response = get_response.json()
    assert json_response['name' == 'Nokia']
    assert json_response['price' == 12500]

E       assert 200 == 400
E        +  where 200 = <Response [200]>.status_code
response   = <Response [200]>
url        = 'https://qa-internship.avito.com/api/1/item'
```
