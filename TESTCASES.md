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
            <td align="left">1. Отправить POST-запрос на эндпоинт "/item" с телом запроса в формате JSON:
		
```
{
"name": "Nokia",
 "price": 12500,
 "sellerId": "test_seller_ID",
	"statistics": {
 	"contacts": 25,
 	"like": 15, 
 	"viewCount": 17
 	}    
} 
```
</td> 
<td rowspan=3 align="left">
	        <ul type="disc">
		    <li>Статус ответа: 200 OK</li>
		    <li>В теле ответа присутствует строка: "Сохранили объявление - ID", где ID это уникальный идентификатор объявления.</li>
	        </ul> 
	    </td>
 	    <td rowspan=3 align="left">Сервер возвращает статус `200`, в ответе присутствует сообщение с ID объявления.</td>
  	    <td rowspan=3 align="center">Check</td>
 	</tr>
        <tr>
            <td align="left">2. Проверить статус ответа.</td>
        </tr>
	<tr>
            <td align="left">3. Извлечь ID созданного объявления из ответа.</td>
        </tr>
        <tr>
            <td rowspan=3 align="center">TC-002</td>
            <td rowspan=3 align="center">Получение объявления по существующему ID (test_get_announce_by_id)</td>
            <td rowspan=3 align="center">Существует объявление с заданным ID</td>
	    <td align="left">1. Отправить GET-запрос на "/item/ID" с корректным идентификатором.</td>
	    <td rowspan=3 align="left">
	    	<ul type="disc">
		    <li>Статус ответа: 200 OK</li>
		    <li>В теле ответа содержится объект с полями 'name', 'price', 'sellerId', 'statistics' и т.д.</li>
	    	</ul>
	    </td>
	    <td rowspan=3 align="left">Если объявление существует, сервер возвращает данные по объявлению.</td>
	    <td rowspan=3 align="center">Check</td>
	</tr>
	    <td align="left">2. Проверить статус ответа.</td>
	<tr>
	    <td align="left">3. Убедиться, что в теле ответа содержится корректная информация о созданном объявлении.</td>
	</tr>
         <tr>
            <td rowspan=3 align="center">TC-003</td>
            <td rowspan=3 align="center">Получение всех объявлений, связанных с ID продавца (test_get_all_announce_by_seller)</td>
            <td rowspan=3 align="center">Существуют объявления, созданные одним продавцом</td>
	    <td align="left">1. Отправить GET-запрос на эндпоинт "/api/1/sellerID/item".</td>
	    <td rowspan=3 align="left">
	    	<ul type="disc">
		    <li>Статус ответа: 200 OK</li>
		    <li>В теле ответа содержится список объявлений данного продавца.</li>
	    	</ul>
	    </td>
	    <td rowspan=3 align="left">Запрос возвращает все объявления продавца корректно.</td>
	    <td rowspan=3 align="center">Check</td>
	</tr>
	    <td align="left">2. Проверить статус ответа.</td>
	<tr>
	    <td align="left">3. Убедиться, что в теле ответа содержатся объекты объявлений.</td>
	</tr>
            <td rowspan=2 align="center">TC-004</td>
            <td rowspan=2 align="center">Создание объявления с некорректными данными (test_post_announce_error_data)</td>
            <td rowspan=2 align="center">Работающий API, валидный "sellerId"</td>
	    <td align="left">1. Отправить POST-запрос на эндпоинт "/item" с телом запроса, в котором отсутствует обязательное поле "price":

```
{
"name": "Телефон",
"sellerId": "<SELLER_ID>",
"statistics": {
	"contacts": 32,
	"like": 35,
	"viewCount": 14
       }
}
```
</td>
<td rowspan=2 align="left">
	    	<ul type="disc">
		    <li>Статус ответа: 400 Bad Request.</li>
		    <li>В теле ответа содержится сообщение об ошибке валидации, указывающее на отсутствие поля 'price'.</li>
	    	</ul>
	    </td>
	    <td rowspan=2 align="left">Сервер корректно возвращает статус 404 с соответствующим сообщением.</td>
	    <td rowspan=2 align="center">Check</td>
	</tr>
	    <td align="left">2. Проверить статус ответа.</td>
            <td rowspan=3 align="center">TC-005</td>
            <td rowspan=3 align="center">Получение объявления с  несуществующим ID (test_get_announce_error_id)</td>
            <td rowspan=3 align="center">Работающий API, ID товара несуществующий</td>
	    <td align="left">1. Отправить GET-запрос на эндпоинт "/item/test_error_ID" с несуществующим ID объявления.</td>
	    <td rowspan=3 align="left">
	    	<ul type="disc">
		    <li>Статус ответа: 404 Not Found.</li>
		    <li>В теле ответа содержится объект с сообщением об ошибке (например, `"item not found"`).</li>
	    	</ul>
	    </td>
	    <td rowspan=3 align="left">Сервер корректно возвращает статус 404 с соответствующим сообщением.</td>
	    <td rowspan=3 align="center">Check</td>
	</tr>
	    <td align="left">2. Проверить статус ответа.</td>
	<tr>
	    <td align="left">3. Убедиться, что в теле ответа содержится сообщение об ошибке.</td>
	</tr>
    </tbody>
</table>
