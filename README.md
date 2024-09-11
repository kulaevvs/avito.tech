## Инструкция к проекту по тестированию API микросервиса

Цель данного проекта - разработка набора автоматизированных тестов для тестирования API микросервиса. Тесты написаны на Python с использованием библиотеки `pytest`. Результатом проекта станет набор автоматизированных тестов, покрывающих основные сценарии использования API микросервиса.

### Основные задачи проекта:

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

### Структура проекта:

- [test_api](/test_api.py) — основной файл, содержащий тесты для тестирования API.
- [TESTCASES.md](/TESTCASES.md) — файл описания тест-кейсов.
- [BUGS.md](/BUGS.md) — файл с баг-репортами для обнаруженных ошибок в API микросервиса.

### Порядок подготовки к запуску тестов (описан порядок для Windows):

1. Клонируйте репозиторий.

        git clone https://github.com/kulaevvs/avito.tech.git

2. Перейдите в директорию проекта.

        cd repository

3. Создайте виртуальное окружение.

        python -m venv venv
   
5. Активируйте виртуальное окружение.

        venv\Scripts\activate

### Запуск тестов:

1. Для запуска тестов используйте команду.

        pytest

При запуске тестового сценария вывод в консоли будет содержать информацию о прохождении или падении тестов, а также подробные сообщения об ошибках, если таковые возникнут. Команда может выполняться с различными ключами, например:

        pytest -v

Запуск тестов с включенным режимом подробного вывода (verbose mode). Это позволяет получить более подробную информацию о ходе выполнения тестов.
        
        pytest -l

Запускает тесты с включенным режимом вывода информации о локальных переменных (local variables). Когда вы запускаете тесты с этим флагом, pytest будет выводить значения локальных переменных в месте, где произошла ошибка или неудачное завершение теста. Это может быть очень полезно при отладке, когда вы хотите понять, какие значения имели переменные в момент возникновения ошибки.

### Описание проводимых тестов при тестировании API:

Тест 1. Наименование: test_post_announce.
Выполняет тестовое создание объявления, содержащего валидные данные. Ожидается успешное создание объявления и возврат статуса 200 OK.

Тест 2. Наименование: test_get_announce_by_id.
Тестирует получение объявления по существующему ID. Ожидается успешное получение данных объявления.

Тест 3. Наименование: test_get_all_announce_by_seller.
Тестирует получение всех объявлений, связанных с продавцом. Ожидается возврат списка объявлений для данного sellerId.

Тест 4. Наименование: test_post_announce_error_data.
Тестирует создание объявления с некорректными данными (без обязательного поля price). Ожидается возврат ошибки валидации со статусом 400 Bad Request.

Тест 5. Наименование: test_get_announce_error_id.
Тестирует получение объявления с несуществующим ID. Ожидается возврат ошибки со статусом 404 Not Found.



