from catalog.models import CartItem, Comment, PreviewItem, ProductDetail, ProductItem
from home.models import Recommendation
from django.shortcuts import render


def catalog(request):

    cartItem1 = CartItem()
    cartItem1.img = "chrome-book-11.jpg"
    cartItem1.imgAltText = "HP Chromebook 11"
    cartItem1.title = "HP Chromebook 11"
    cartItem1.label = "Laptops"
    cartItem1.price = 199.99
    cartItem1.quantity = 2

    cartItem2 = CartItem()
    cartItem2.img = "chrome-book-14.jpg"
    cartItem2.imgAltText = "HP Chromebook 14"
    cartItem2.title = "HP Chromebook 14"
    cartItem2.label = "Laptops"
    cartItem2.price = 209.99
    cartItem2.quantity = 1

    cartItem3 = CartItem()
    cartItem3.img = "ipad-air.jpg"
    cartItem3.imgAltText = "iPad Air"
    cartItem3.title = "iPad Air"
    cartItem3.label = "Tablets"
    cartItem3.price = 449.99
    cartItem3.quantity = 2

    cartItem4 = CartItem()
    cartItem4.img = "mi-pad-2.jpg"
    cartItem4.imgAltText = "Mi Pad 2"
    cartItem4.title = "Mi Pad 2"
    cartItem4.label = "Tablets"
    cartItem4.price = 199.99
    cartItem4.quantity = 3

    cartItems = [cartItem1, cartItem2, cartItem3, cartItem4]

    productItem1 = ProductItem()
    productItem1.img = "ipad-air.jpg"
    productItem1.imgAltText = "iPad Air"
    productItem1.isFavorite = False
    productItem1.title = "iPad Air"
    productItem1.sale = 299.99
    productItem1.isOffer = True
    productItem1.priceThrough = 349.99
    productItem1.label = "Tablets"

    productItem2 = ProductItem()
    productItem2.img = "chrome-book-asus.jpg"
    productItem2.imgAltText = "ASUS Chromebook"
    productItem2.isFavorite = True
    productItem2.title = "Asus Chromebook"
    productItem2.sale = 299.99
    productItem2.isOffer = False
    productItem2.label = "Laptops"

    productItems = [productItem1, productItem2]

    return render(request, 'catalog/catalog.html', {'cartItems': cartItems, 'productItems': productItems})


def product(request):

    productDetail = ProductDetail()
    productDetail.title = "HP Chromebook 11"
    productDetail.brandLogo = "hp.png"
    productDetail.brandLogoAltText = "HP"
    productDetail.subTitle1 = "Chrome OS™"
    productDetail.subTitle2 = "Intel® Celeron® processor"
    productDetail.subTitle3 = "Intel HD Graphics"
    productDetail.sale = 209.99
    productDetail.isOffer = True
    productDetail.priceThrough = 249.99
    productDetail.desc = "The stylish HP Chromebook provides a speedy connection to your protected online content and automatically updated apps, all within an ultra-thin full-sized notebook, providing a comfortable gateway to surf, socialize and play."
    productDetail.osDetail = "Chrome OS™"
    productDetail.processorDetial = "Intel® Celeron® N2840 with Intel® HD Graphics (2.16 GHz, up to 2.58 GHz, 1 MB cache, 2 cores)"
    productDetail.processorTechDetial = "Intel Turbo Boost Technology"
    productDetail.graphicsDetail = "Intel HD Graphics"
    productDetail.memoryDetail = "2 GB DDR3L SDRAM (onboard)"
    productDetail.harddriveDetail = "16 GB eMMC"
    productDetail.wirelessDetail = "802.11ac (2x2) and Bluetooth® 4.0 combo"
    productDetail.powerSupplyDetail = "45 W AC power adapter"
    productDetail.batteryDetail = "3-cell, 36 Wh Li-ion"

    cartItem1 = CartItem()
    cartItem1.img = "chrome-book-11.jpg"
    cartItem1.imgAltText = "HP Chromebook 11"
    cartItem1.title = "HP Chromebook 11"
    cartItem1.label = "Laptops"
    cartItem1.price = 199.99
    cartItem1.quantity = 2

    cartItem2 = CartItem()
    cartItem2.img = "chrome-book-14.jpg"
    cartItem2.imgAltText = "HP Chromebook 14"
    cartItem2.title = "HP Chromebook 14"
    cartItem2.label = "Laptops"
    cartItem2.price = 209.99
    cartItem2.quantity = 1

    cartItem3 = CartItem()
    cartItem3.img = "ipad-air.jpg"
    cartItem3.imgAltText = "iPad Air"
    cartItem3.title = "iPad Air"
    cartItem3.label = "Tablets"
    cartItem3.price = 449.99
    cartItem3.quantity = 2

    cartItem4 = CartItem()
    cartItem4.img = "mi-pad-2.jpg"
    cartItem4.imgAltText = "Mi Pad 2"
    cartItem4.title = "Mi Pad 2"
    cartItem4.label = "Tablets"
    cartItem4.price = 199.99
    cartItem4.quantity = 3

    cartItems = [cartItem1, cartItem2, cartItem3, cartItem4]

    previewItem1 = PreviewItem()
    previewItem1.dataMarker = 1
    previewItem1.isActive = True
    previewItem1.img = "1.jpg"
    previewItem1.imgAltText = "ChromeBook 11"

    previewItem2 = PreviewItem()
    previewItem2.dataMarker = 2
    previewItem2.img = "2.jpg"
    previewItem2.imgAltText = "ChromeBook 11"

    previewItem3 = PreviewItem()
    previewItem3.dataMarker = 3
    previewItem3.img = "3.jpg"
    previewItem3.imgAltText = "ChromeBook 11"

    previewItem4 = PreviewItem()
    previewItem4.dataMarker = 4
    previewItem4.isVideo = True
    previewItem4.videoId = "hED0N4CFoqs"
    previewItem4.videoTitle = "An upscale new Chromebook from HP"
    previewItem4.videoDesc = "The new HP Chromebook 13 runs a Core M CPU inside a slim aluminum body."
    previewItem4.videoThumbImg = "video.jpg"
    previewItem4.videoThumbImgAltText = "ChromeBook 11"

    previewItem5 = PreviewItem()
    previewItem5.dataMarker = 5
    previewItem5.isVideo = True
    previewItem5.videoId = "hED0N4CFoqs"
    previewItem5.videoTitle = "An upscale new Chromebook from HP"
    previewItem5.videoDesc = "The new HP Chromebook 13 runs a Core M CPU inside a slim aluminum body."
    previewItem5.videoThumbImg = "video.jpg"
    previewItem5.videoThumbImgAltText = "ChromeBook 11"

    previewItems = [
        previewItem1, previewItem2, previewItem3, previewItem4, previewItem5,
    ]

    recommend1 = Recommendation()
    recommend1.isFavorite = False
    recommend1.headline = "HP Chromebook 11"
    recommend1.isOffer = False
    recommend1.sale = 199.99
    recommend1.label = "Laptops"
    recommend1.img = "chrome-book-11.jpg"
    recommend1.imgAltText = "HP Chromebook 11"

    recommend2 = Recommendation()
    recommend2.isFavorite = True
    recommend2.headline = "HP Chromebook 14"
    recommend2.isOffer = True
    recommend2.sale = 209.99
    recommend2.priceThrough = 249.99
    recommend2.label = "Laptops"
    recommend2.img = "chrome-book-14.jpg"
    recommend2.imgAltText = "HP Chromebook 14"

    recommend3 = Recommendation()
    recommend3.isFavorite = False
    recommend3.headline = "Asus Chromebook"
    recommend3.isOffer = False
    recommend3.sale = 299.99
    recommend3.label = "Laptops"
    recommend3.img = "chrome-book-asus.jpg"
    recommend3.imgAltText = "ASUS Chromebook"

    recommend4 = Recommendation()
    recommend4.isFavorite = True
    recommend4.headline = "HP Chromebook 14"
    recommend4.isOffer = True
    recommend4.sale = 209.99
    recommend4.priceThrough = 249.99
    recommend4.label = "Laptops"
    recommend4.img = "chrome-book-14.jpg"
    recommend4.imgAltText = "HP Chromebook 14"

    recommends = [recommend1, recommend2, recommend3, recommend4]

    comment1 = Comment()
    comment1.authorName = "Chris Hemsworth"
    comment1.date = "Today"
    comment1.desc = "Samsung's Galaxy S7 smartphone is getting serious hype. Here's what it does better than Apple's iPhone 6s."

    comment2 = Comment()
    comment2.authorName = "Anne Hathaway"
    comment2.date = "2 years ago"
    comment2.desc = "Apple Music brings iTunes music streaming to the UK. But is it worth paying for? In our Apple Music review, we examine the service's features, UK pricing, audio quality and music library"

    comment3 = Comment()
    comment3.authorName = "Anne Hathaway"
    comment3.date = "2 years ago"
    comment3.desc = "Apple Music brings iTunes music streaming to the UK. But is it worth paying for? In our Apple Music review, we examine the service's features, UK pricing, audio quality and music library"

    comments = [comment1, comment2, comment3]

    return render(request, 'catalog/product.html', {'productDetail': productDetail, 'cartItems': cartItems, 'previewItems': previewItems, 'recommends': recommends, 'comments': comments})
