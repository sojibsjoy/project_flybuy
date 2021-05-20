from django.db import models

class ProductItem:
    isFavorite: bool
    img: str
    imgAltText: str
    title: str
    sale: float
    isOffer: bool
    priceThrough: float
    label: str


class ProductDetail:
    title: str
    brandLogo: str
    brandLogoAltText: str
    subTitle1: str
    subTitle2: str
    subTitle3: str
    sale: float
    isOffer: bool
    priceThrough: float
    desc: str
    osDetail: str
    processorDetial: str
    processorTechDetial: str
    graphicsDetail: str
    memoryDetail: str
    harddriveDetail: str
    wirelessDetail: str
    powerSupplyDetail: str
    batteryDetail: str


class PreviewItem:
    dataMarker: int
    isActive: bool
    isVideo: bool
    videoId: str
    videoTitle: str
    videoDesc: str
    videoThumbImg: str
    videoThumbImgAltText: str
    img: str
    imgAltText: str


class Comment:
    authorName: str
    date: str
    desc: str
