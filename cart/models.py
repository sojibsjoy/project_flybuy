from django.db import models


class CartItem:
    img: str
    imgAltText: str
    title: str
    label: str
    price: float
    quantity: int
