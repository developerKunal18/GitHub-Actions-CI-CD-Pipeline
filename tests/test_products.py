from app import db
from app.models import Product

def test_products(client, app):
    with app.app_context():
        db.session.add(Product(name="Running Shoes", price=4999))
        db.session.commit()

    response = client.get("/products")
    assert response.status_code == 200

    products = response.get_json()
    assert len(products) == 1
    assert products[0]["name"] == "Running Shoes"
    assert products[0]["price"] == 4999
