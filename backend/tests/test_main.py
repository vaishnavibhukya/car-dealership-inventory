from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


# =========================================================
# 1. Health Check
# =========================================================

def test_health_check():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "API is running"
    }


# =========================================================
# 2. Get all cars
# =========================================================

def test_get_all_cars():
    response = client.get("/cars/")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


# =========================================================
# 3. Create car
# =========================================================

def test_create_car():
    response = client.post(
        "/cars/",
        json={
            "make": "Toyota",
            "model": "Camry",
            "year": 2022,
            "price": 25000,
            "mileage": 10000,
            "color": "White",
            "status": "available"
        }
    )

    assert response.status_code == 200

    car = response.json()

    assert car["make"] == "Toyota"
    assert car["model"] == "Camry"
    assert car["year"] == 2022
    assert car["price"] == 25000
    assert car["mileage"] == 10000
    assert car["color"] == "White"
    assert car["status"] == "available"


# =========================================================
# 4. Get car by ID
# =========================================================

def test_get_car():
    create_response = client.post(
        "/cars/",
        json={
            "make": "Honda",
            "model": "Civic",
            "year": 2023,
            "price": 28000,
            "mileage": 5000,
            "color": "Black",
            "status": "available"
        }
    )

    assert create_response.status_code == 200

    car_id = create_response.json()["id"]

    response = client.get(f"/cars/{car_id}")

    assert response.status_code == 200
    assert response.json()["id"] == car_id


# =========================================================
# 5. Get non-existing car
# =========================================================

def test_get_non_existing_car():
    response = client.get("/cars/999999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Car not found"


# =========================================================
# 6. Update car
# =========================================================

def test_update_car():
    create_response = client.post(
        "/cars/",
        json={
            "make": "Ford",
            "model": "Focus",
            "year": 2021,
            "price": 20000,
            "mileage": 15000,
            "color": "Blue",
            "status": "available"
        }
    )

    car_id = create_response.json()["id"]

    response = client.put(
        f"/cars/{car_id}",
        json={
            "make": "Ford",
            "model": "Mustang",
            "year": 2024,
            "price": 45000,
            "mileage": 1000,
            "color": "Red",
            "status": "reserved"
        }
    )

    assert response.status_code == 200

    car = response.json()

    assert car["id"] == car_id
    assert car["model"] == "Mustang"
    assert car["year"] == 2024
    assert car["price"] == 45000
    assert car["status"] == "reserved"


# =========================================================
# 7. Update non-existing car
# =========================================================

def test_update_non_existing_car():
    response = client.put(
        "/cars/999999",
        json={
            "make": "Toyota",
            "model": "Corolla",
            "year": 2022,
            "price": 22000,
            "mileage": 10000,
            "color": "White",
            "status": "available"
        }
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Car not found"


# =========================================================
# 8. Delete car
# =========================================================

def test_delete_car():
    create_response = client.post(
        "/cars/",
        json={
            "make": "BMW",
            "model": "X5",
            "year": 2023,
            "price": 60000,
            "mileage": 5000,
            "color": "Black",
            "status": "available"
        }
    )

    car_id = create_response.json()["id"]

    response = client.delete(f"/cars/{car_id}")

    assert response.status_code == 200

    assert response.json() == {
        "message": "Car deleted successfully"
    }

    get_response = client.get(f"/cars/{car_id}")

    assert get_response.status_code == 404


# =========================================================
# 9. Delete non-existing car
# =========================================================

def test_delete_non_existing_car():
    response = client.delete("/cars/999999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Car not found"


# =========================================================
# 10. Make filter
# =========================================================

def test_make_filter():
    response = client.get("/cars/?make=Toyota")

    assert response.status_code == 200

    cars = response.json()

    for car in cars:
        assert "toyota" in car["make"].lower()


# =========================================================
# 11. Status filter
# =========================================================

def test_status_filter():
    response = client.get("/cars/?status=available")

    assert response.status_code == 200

    cars = response.json()

    for car in cars:
        assert car["status"] == "available"


# =========================================================
# 12. Color filter
# =========================================================

def test_color_filter():
    response = client.get("/cars/?color=red")

    assert response.status_code == 200

    cars = response.json()

    for car in cars:
        assert "red" in car["color"].lower()


# =========================================================
# 13. Minimum price filter
# =========================================================

def test_min_price_filter():
    response = client.get(
        "/cars/?min_price=20000"
    )

    assert response.status_code == 200

    cars = response.json()

    for car in cars:
        assert car["price"] >= 20000


# =========================================================
# 14. Maximum price filter
# =========================================================

def test_max_price_filter():
    response = client.get(
        "/cars/?max_price=50000"
    )

    assert response.status_code == 200

    cars = response.json()

    for car in cars:
        assert car["price"] <= 50000


# =========================================================
# 15. Price range filter
# =========================================================

def test_price_range_filter():
    response = client.get(
        "/cars/?min_price=20000&max_price=50000"
    )

    assert response.status_code == 200

    cars = response.json()

    for car in cars:
        assert 20000 <= car["price"] <= 50000


# =========================================================
# 16. Negative price validation
# =========================================================

def test_negative_price():
    response = client.post(
        "/cars/",
        json={
            "make": "Toyota",
            "model": "Camry",
            "year": 2022,
            "price": -1000,
            "mileage": 10000,
            "color": "White",
            "status": "available"
        }
    )

    assert response.status_code == 422


# =========================================================
# 17. Negative mileage validation
# =========================================================

def test_negative_mileage():
    response = client.post(
        "/cars/",
        json={
            "make": "Toyota",
            "model": "Camry",
            "year": 2022,
            "price": 25000,
            "mileage": -100,
            "color": "White",
            "status": "available"
        }
    )

    assert response.status_code == 422


# =========================================================
# 18. Invalid year
# =========================================================

def test_invalid_year():
    response = client.post(
        "/cars/",
        json={
            "make": "Toyota",
            "model": "Camry",
            "year": 1800,
            "price": 25000,
            "mileage": 10000,
            "color": "White",
            "status": "available"
        }
    )

    assert response.status_code == 422


# =========================================================
# 19. Invalid status
# =========================================================

def test_invalid_status():
    response = client.post(
        "/cars/",
        json={
            "make": "Toyota",
            "model": "Camry",
            "year": 2022,
            "price": 25000,
            "mileage": 10000,
            "color": "White",
            "status": "invalid"
        }
    )

    assert response.status_code == 422


# =========================================================
# 20. Empty make
# =========================================================

def test_empty_make():
    response = client.post(
        "/cars/",
        json={
            "make": "",
            "model": "Camry",
            "year": 2022,
            "price": 25000,
            "mileage": 10000,
            "color": "White",
            "status": "available"
        }
    )

    assert response.status_code == 422


# =========================================================
# 21. Missing required field
# =========================================================

def test_missing_required_field():
    response = client.post(
        "/cars/",
        json={
            "model": "Camry",
            "year": 2022,
            "price": 25000,
            "mileage": 10000,
            "color": "White",
            "status": "available"
        }
    )

    assert response.status_code == 422


# =========================================================
# 22. Year too high
# =========================================================

def test_year_too_high():
    response = client.post(
        "/cars/",
        json={
            "make": "Toyota",
            "model": "Camry",
            "year": 2200,
            "price": 25000,
            "mileage": 10000,
            "color": "White",
            "status": "available"
        }
    )

    assert response.status_code == 422


# =========================================================
# 23. Pagination
# =========================================================

def test_pagination():
    response = client.get(
        "/cars/?skip=0&limit=2"
    )

    assert response.status_code == 200

    cars = response.json()

    assert len(cars) <= 2


# =========================================================
# 24. Pagination with skip
# =========================================================

def test_pagination_skip():
    response = client.get(
        "/cars/?skip=1&limit=2"
    )

    assert response.status_code == 200

    cars = response.json()

    assert len(cars) <= 2


# =========================================================
# 25. Pagination limit
# =========================================================

def test_pagination_limit():
    response = client.get(
        "/cars/?limit=1"
    )

    assert response.status_code == 200

    cars = response.json()

    assert len(cars) <= 1


# =========================================================
# 26. Negative skip
# =========================================================

def test_negative_skip():
    response = client.get(
        "/cars/?skip=-1&limit=10"
    )

    assert response.status_code == 400

    assert response.json()["detail"] == "skip cannot be negative"


# =========================================================
# 27. Limit greater than 100
# =========================================================

def test_limit_too_high():
    response = client.get(
        "/cars/?skip=0&limit=101"
    )

    assert response.status_code == 400

    assert response.json()["detail"] == (
        "limit must be between 1 and 100"
    )


# =========================================================
# 28. Limit equal to zero
# =========================================================

def test_limit_zero():
    response = client.get(
        "/cars/?skip=0&limit=0"
    )

    assert response.status_code == 400

    assert response.json()["detail"] == (
        "limit must be between 1 and 100"
    )


# =========================================================
# 29. Combined filter + pagination
# =========================================================

def test_filter_with_pagination():
    response = client.get(
        "/cars/?make=Toyota&skip=0&limit=5"
    )

    assert response.status_code == 200

    cars = response.json()

    assert len(cars) <= 5

    for car in cars:
        assert "toyota" in car["make"].lower()


# =========================================================
# 30. Price filter + pagination
# =========================================================

def test_price_filter_with_pagination():
    response = client.get(
        "/cars/?min_price=20000&max_price=50000&limit=5"
    )

    assert response.status_code == 200

    cars = response.json()

    assert len(cars) <= 5

    for car in cars:
        assert 20000 <= car["price"] <= 50000


# =========================================================
# 31. Status filter + pagination
# =========================================================

def test_status_filter_with_pagination():
    response = client.get(
        "/cars/?status=available&limit=5"
    )

    assert response.status_code == 200

    cars = response.json()

    assert len(cars) <= 5

    for car in cars:
        assert car["status"] == "available"


# =========================================================
# 32. Color filter + pagination
# =========================================================

def test_color_filter_with_pagination():
    response = client.get(
        "/cars/?color=red&limit=5"
    )

    assert response.status_code == 200

    cars = response.json()

    assert len(cars) <= 5

    for car in cars:
        assert "red" in car["color"].lower()


# =========================================================
# 33. All filters + pagination
# =========================================================

def test_all_filters_with_pagination():
    response = client.get(
        "/cars/"
        "?make=Toyota"
        "&status=available"
        "&color=red"
        "&min_price=10000"
        "&max_price=100000"
        "&skip=0"
        "&limit=5"
    )

    assert response.status_code == 200

    cars = response.json()

    assert len(cars) <= 5

    for car in cars:
        assert "toyota" in car["make"].lower()
        assert car["status"] == "available"
        assert "red" in car["color"].lower()
        assert 10000 <= car["price"] <= 100000


# =========================================================
# 34. Test Purchase Car
# =========================================================

def test_purchase_car():
    response = client.post("/cars/1/purchase")

    assert response.status_code == 200

    car = response.json()

    assert car["id"] == 1
    assert car["status"] == "sold"


# =========================================================
# 35. Test Purchase Already Sold Car
# =========================================================

def test_purchase_already_sold_car():
    response = client.post("/cars/1/purchase")

    assert response.status_code == 400

    assert response.json()["detail"] == "Car is already sold"


# =========================================================
# 36. Test Restock Car
# =========================================================

def test_restock_car():
    response = client.post("/cars/1/restock")

    assert response.status_code == 200

    car = response.json()

    assert car["id"] == 1
    assert car["status"] == "available"


# =========================================================
# 37. Test Restock Already Available Car
# =========================================================

def test_restock_already_available_car():
    response = client.post("/cars/1/restock")

    assert response.status_code == 400

    assert response.json()["detail"] == "Car is already available"


# =========================================================
# 38. Test Purchase Non Existing Car
# =========================================================

def test_purchase_non_existing_car():
    response = client.post("/cars/99999/purchase")

    assert response.status_code == 404

    assert response.json()["detail"] == "Car not found"


# =========================================================
# 39. Test Restock Non Existing Car
# =========================================================

def test_restock_non_existing_car():
    response = client.post("/cars/99999/restock")

    assert response.status_code == 404

    assert response.json()["detail"] == "Car not found"