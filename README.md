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

#### Обеспечение стабильности и надежности API микросервиса
<u>Выявление и устранение ошибок и уязвимостей в API</u>
<u>Обеспечение соответствия API спецификациям и требованиям</u>

#### Повышение качества разработки и поддержки API микросервиса
<u>Автоматизация процесса тестирования API</u>

### Структура проекта:

- pytest_api — основной файл, содержащий тесты для тестирования API.
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

        venv\Scripts\activate.bat

### Запуск тестов:

1. Для запуска тестов используйте команду.

        pytest

### Запуск тестов:

