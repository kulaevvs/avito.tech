# Импорт библиотек для выполнения тестов
import pytest
import requests

# Сведения для выполнения тестов, пояснения содержатся в README.md
test_base_URL = "https://qa-internship.avito.com/api/1"
test_seller_ID = 987531
test_error_ID = "09209618-5494-488e-89f3-966366b361a7_35"
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
test_error_payload = {
    "name": "Nokia",
    "sellerId": test_seller_ID,
    "statistics": {
        "contacts": 25,
        "likes": 15,
        "viewCount": 17    
    }
}

# Создаём функцию, выполняющую предварительную настройку для тестов
@pytest.fixture
def create_announce():
    response = requests.post(f"{test_base_URL}/item", json=test_payload, timeout=5)
    assert response.status_code == 200
    listing_id = response.json()["status"].split(' - ')[1]
    return listing_id

# Выполняем тест на создание объявления
def test_post_announce():
    """Тест на создание объявления"""
    url = f"{test_base_URL}/item"
    response = requests.post(url, json=test_payload, timeout=5)
    assert response.status_code == 200
    json_response = response.json()
    assert "id" in json_response

# Выполняем тест на получение объявления по его ID
def test_get_announce_by_id(create_announce):
    """Тест на получение объявления по ID"""
    get_url = f"{test_base_URL}/item/{create_announce}"
    get_response = requests.get(get_url, timeout=5)
    assert get_response.status_code == 200
    json_response = get_response.json()
    assert json_response['name' == 'Nokia']
    assert json_response['price' == 12500]

# Выполняем тест на получение всех объявлений по ID продавца (с генерацией 3-х дополнительных записей)
def test_get_all_announce_by_seller():
    """Тест на получение всех объявлений по продавцу (с генерацией 3-х дополнительных записей)"""
    for i in range(3):
        payload = {
            "name": f"Product {i}",
            "price": 10000 + i * 1000,
            "sellerId": test_seller_ID,
            "statistics": {
                "contacts": 10 + i,
                "likes": 5 + i,
                "viewCount": 20 + i
            }
        }
        response = requests.post(f"{test_base_URL}/item", json=payload, timeout=5)
        assert response.status_code == 200
    get_url = f"{test_base_URL}/{test_seller_ID}/item"
    get_response = requests.get(get_url, timeout=5)
    assert get_response.status_code == 200
    listings = get_response.json()
    assert len(listings) >= 3

# Выполняем тест на создание объявления с некорректными данными
def test_post_announce_error_data():
    """Тест на создание объявления с некорректными данными (отсутствует поле 'price')"""
    url = f"{test_base_URL}/item"
    response = requests.post(url, json=test_error_payload, timeout=5)
    assert response.status_code == 400

# Выполняем тест на получение объявления с несуществующим ID
def test_get_announce_error_id():
    """Тест на получение объявления с несуществующим ID"""
    get_url = f"{test_base_URL}/item/{test_error_ID}"
    response = requests.get(get_url, timeout=5)
    assert response.status_code == 404
    assert "message" in response.json()["result"]
