from django.db import models


class Summary:
    subTotal: float
    discount: float
    delivery: float
    total: float


class DeliveryAddress:
    isSelected: bool
    name: str
    country: str
    city: str
    street: str
    building: str
    zipCode: int


class DeliveryOption:
    isSelected: bool
    img: str
    imgTitle: str
    imgAltText: str
    desc: str


class PaymentMethod:
    isSelected: bool
    img: str
    imgTitle: str
    imgAltText: str
    desc: str
