## Инструкция к проекту по тестированию API микросервиса

Цель данного проекта - разработка набора автоматизированных тестов для тестирования API микросервиса. Тесты написаны на Python с использованием библиотеки `pytest`. Результатом проекта станет набор автоматизированных тестов, покрывающих основные сценарии использования API микросервиса.

### Основные задачи проекта:

#### Проверка корректности работы различных эндпоинтов API микросервиса:
        Проверка возвращаемых HTTP-кодов ответов
        Проверка структуры и содержимого ответов в формате JSON

#### Тестирование различных сценариев использования API:
        Проверка работы API при передаче корректных данных
        Проверка работы API при передаче некорректных данных
        Проверка работы API при выполнении CRUD-операций (Create, Read, Update, Delete)

#### Обеспечение стабильности и надежности API микросервиса:
        Выявление и устранение ошибок и уязвимостей в API
        Обеспечение соответствия API спецификациям и требованиям

#### Повышение качества разработки и поддержки API микросервиса:
        Автоматизация процесса тестирования API

### Структура проекта:

- pytest_api — основной файл, содержащий тесты для тестирования API.
- [TESTCASES.md](/TESTCASES.md) — файл описания тест-кейсов.
- BUGS.md — файл с баг-репортами для обнаруженных ошибок в API микросервиса.

### Порядок подготовки к запуску тестов:
