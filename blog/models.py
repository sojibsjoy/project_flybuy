from django.db import models


class Article:
    isPhotoArticle: bool
    isVideoArticle: bool
    isReviewArticle: bool
    img: str
    imgTitle: str
    imgAltText: str
    headline: str
    date: str
    desc: str
