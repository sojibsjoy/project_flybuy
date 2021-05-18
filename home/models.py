from django.db import models


class SlideItem:
    centerPosition: bool
    leftPosition: bool
    rightPosition: bool
    dataMarker: int
    title: str
    subTitle: str
    imgPrimary: str
    imgSecondary: str
    imgAltText: str


class NewProducts:
    isFavorite: bool
    headline: str
    isOffer: bool
    sale: float
    priceThrough: float
    label: str
    img: str
    imgAltText: str


class Recommendation:
    isFavorite: bool
    headline: str
    isOffer: bool
    sale: float
    priceThrough: float
    label: str
    img: str
    imgAltText: str


class NewArticle:
    isPhotoArticle: bool
    isVideoArticle: bool
    isReviewArticle: bool
    img: str
    imgTitle: str
    imgAltText: str
    headline: str
    date: str
    desc: str
