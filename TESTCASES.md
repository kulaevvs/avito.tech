## Тест-кейсы для тестирования API микросервиса

<table>
    <thead>
        <tr>
            <th>Test Case ID</th>
            <th>Описание тест-кейса</th>
            <th>Тестовые данные</th>
            <th>Шаги воспроизведения</th>
            <th>Ожидаемый результат</th>
            <th>Фактический результат</th>
            <th>Статус прохождения</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan=3 align="center">TC-001</td>
            <td rowspan=3 align="center">Создание объявления (test_post_announce)</td>
            <td rowspan=3 align="center">Работающий API, валидный "sellerId"</td>
            <td align="left">1. Отправить POST-запрос на эндпоинт '/item' с телом запроса в формате JSON:
		    
	{"name": "Nokia",
	 "price": 12500,
	 "sellerId": "test_seller_ID",
  		"statistics": {
	 	"contacts": 25,
	 	"like": 15, 
	 	"viewCount": 17
	 	}    
	} 
</td>
	<td align="left">
	    <ul type="disc">
		<li>Статус ответа: `200 OK`</li>
		<li>В теле ответа присутствует строка: `"Сохранили объявление - <ID>"`, где `<ID>` — это уникальный идентификатор объявления.</li>
	    </ul> 
	</td>
 	<td align="left">Сервер возвращает статус `200`, в ответе присутствует сообщение с ID объявления.</td>
 	</tr>
        <tr>
            <td align="left">2. Проверить статус ответа.</td>
        </tr>
	<tr>
            <td align="left">3. Извлечь ID созданного объявления из ответа.</td>
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
