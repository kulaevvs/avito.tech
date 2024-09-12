## Тест-кейсы для тестирования API микросервиса

### Тест-кейс № 1

<table>
    <thead>
        <tr>
            <th>Column 1</th>
            <th>Column 2</th>
            <th>Column 3</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan=4 align="center">R1 Text</td>
            <td rowspan=2 align="center">R2 Text A</td>
            <td align="center">R3 Text A</td>
        </tr>
        <tr>
            <td align="center">R3 Text B</td>
        </tr>
        <tr>
            <td rowspan=2 align="center">R2 Text B</td>
            <td align="center">R3 Text C</td>
        </tr>
        <tr>
            <td align="center">R3 Text D</td>
        </tr>
    </tbody>
</table>

|Test Case ID|Описание тест-кейса|Тестовые данные|Шаги воспроизведения|Ожидаемый результат|Фактический результат|Статус прохождения|
|---|---|---|---|---|---|---|
|TC-001      |Создание объявления (test_post_announce)|Работающий API, валидный 'sellerId'|1. Отправить POST-запрос на эндпоинт `/item` с телом запроса в формате JSON: ```{   {"name": "Nokia", "price": 12500, "sellerId": "test_seller_ID", "statistics": {"contacts": 25, "like": 15, "viewCount": 17}  }```  2. Проверить статус ответа.  3. Извлечь ID созданного объявления из ответа.
|TC-002      |Получение объявления по существующему ID (test_get_announce_by_id)|   |   |   |
|TC-003      |Получение всех объявлений, связанных с ID продавца (test_get_all_announce_by_seller)|   |   |   |
|TC-004      |Создание объявления с некорректными данными (test_post_announce_error_data)|
|TC-005      |Gолучение объявления с  несуществующим ID (test_get_announce_error_id)|
