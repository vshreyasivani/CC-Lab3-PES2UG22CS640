import json
from cart import dao
from products import Product


class Cart:
    def __init__(self, id: int, username: str, contents: list[Product], cost: float):
        self.id = id
        self.username = username
        self.contents = contents
        self.cost = cost

    @staticmethod
    def load(data: dict):
        products_list = [Product(**item) for item in json.loads(data['contents'])]
        return Cart(data['id'], data['username'], products_list, data['cost'])


def get_cart(username: str) -> list[Product]:
    cart_details = dao.get_cart(username)
    if not cart_details:
        return []

    
    items = [
        products.get_product(product_id)
        for cart_detail in cart_details
        for product_id in json.loads(cart_detail['contents'])
    ]
    return items


def add_to_cart(username: str, product_id: int):
    dao.add_to_cart(username, product_id)


def remove_from_cart(username: str, product_id: int):
    dao.remove_from_cart(username, product_id)


def delete_cart(username: str):
    dao.delete_cart(username)
