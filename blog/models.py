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


class PhotoBlogItem:
    img: str
    imgAltText: str
    headline: str
    bodyText: str


class PhotoBlogComment:
    authorName: str
    date: str
    comment: str


class VideoBlogItem:
    id: str
    title: str
    desc: str
    thumbImg: str
    thumbImgAltText: str
    headline: str
    bodyText: str


class VideoBlogComment:
    authorName: str
    date: str
    comment: str


class ReviewBlogItem:
    title: str
    titleDesc: str
    isVideoAvailable: bool
    videoId: str
    thumbImg: str
    thumbImgAltText: str
    videoTitle: str
    videoDesc: str
    startingPrice: float
    ffFlag: bool
    ffTitle1: str
    ffTitle2: str
    ffImg: str
    ffImgAltText: str
    ffDesc: str
    sfFlag: bool
    sfTitle1: str
    sfTitle2: str
    sfImg: str
    sfImgAltText: str
    sfDesc: str
    thFlag: bool
    tfTitle1: str
    tfTitle2: str
    tfImg: str
    tfImgAltText: str
    tfDesc: str
    bottomHeadline: str
    bottomText: str


class ReviewProduct:
    isFavorite: bool
    img: str
    imgAltText: str
    title: str
    sale: float
    isOffer: bool
    priceThrough: float
    label: str
