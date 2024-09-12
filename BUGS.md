## Баг-репорт по результатам тестирования API микросервиса

### Таблица содержит следующие колонки:
- ID
- Приоритет бага (high, medium, low)
- Серьёзность
- Скрипт/Модуль
- Описание бага
- Шаги воспроизведения
- Фактический результат
- Ожидаемый результат

<table>
    <thead>
        <tr>
            <th>ID</th>
            <th>Приоритет бага (high, medium, low)</th>
            <th>Серьёзность</th>
            <th>Скрипт/Модуль</th>
            <th>Описание бага</th>
            <th>Шаги воспроизведения</th>
            <th>Фактический результат</th>
            <th>Ожидаемый результат</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan=3 align="center">B-001</td>
            <td rowspan=3 align="center">High</td>
            <td rowspan=3 align="center">Блокирующий для дальнейшего тестирования получения объявления по ID</td>
	    <td rowspan=3 align="center">test_api.py::test_post_announce</td>
	    <td rowspan=3 align="center">Отсутствует поле 'id' в ответе на создание объявления</td>
            <td align="left">1. Отправить POST-запрос на создание объявления по URL "https://qa-internship.avito.com/api/item".</td> 
	    <td rowspan=3 align="left">В ответе присутствует сообщение о сохранении объявления, но отсутствует 'id'</td>
 	    <td rowspan=3 align="left">В теле ответа присутствует уникальный 'id' созданного объявления</td>
 	</tr>
        <tr>
            <td align="left">2. В теле запроса передать валидные данные в формате JSON:

```
{
"name": "Nokia",
"price": 12500,
"sellerId": test_seller_ID,
"statistics": {
         "contacts": 25,
         "like": 15,
         "viewCount": 17
	}
}
```
</td> 
	</tr>
	<tr>
            <td align="left">3. Получить ответ от сервера.</td>
        </tr>
	<tr>
            <td rowspan=3 align="center">B-002</td>
            <td rowspan=3 align="center">Medium</td>
            <td rowspan=3 align="center">Ошибка в валидации данных</td>
	    <td rowspan=3 align="center">test_api.py::test_post_announce_error_data</td>
	    <td rowspan=3 align="center">Сервер возвращает статус 200 OK, при отправке запроса с некорректными данными</td>
            <td align="left">1. Отправить POST-запрос на создание объявления по URL "https://qa-internship.avito.com/api/item".</td> 
	    <td rowspan=3 align="left">Сервер возвращает статус 200 OK, что означает успешное выполнение запроса</td>
 	    <td rowspan=3 align="left">Сервер возвращет статус 400 Bad Request, так как отсутствует обязательное поле 'price'</td>
 	</tr>
        <tr>
            <td align="left">2. В теле запроса передать валидные данные в формате JSON:

```
{
"name": "Nokia",
"sellerId": test_seller_ID,
"statistics": {
         "contacts": 25,
         "like": 15,
         "viewCount": 17
	}
}
```
</td> 
	</tr>
	<tr>
            <td align="left">3. Получить ответ от сервера.</td>
        </tr>
	<tr>
            <td rowspan=3 align="center">B-003</td>
            <td rowspan=3 align="center">Low</td>
            <td rowspan=3 align="center">Не соответствующий стандартам обработки ошибок API</td>
	    <td rowspan=3 align="center">test_api.py:test_get_announce_error_id</td>
	    <td rowspan=3 align="center">Некорректный ответ при получении объявления с несуществующим ID</td>
            <td align="left">1. Отправить GET-запрос на получение объявления по несуществующему ID. В тестовом запросе URL "https://qa-internship.avito.com/api/item/09209618-5494-488e-89f3-966366b361a7_35".</td> 
	    <td rowspan=3 align="left">Сервер возвращает статус 404 Not Found, без поля error и кода ошибки</td>
 	    <td rowspan=3 align="left">Сервер возвращает статус 404 Not Found, с полем error и кодом ошибки</td>
 	</tr>
        <tr>
            <td align="left">2. Получить ответ от сервера.</td> 
	</tr>
    </tbody>
</table>
