from django.shortcuts import render
from blog.models import Article, PhotoBlogComment, PhotoBlogItem, ReviewBlogItem, ReviewProduct, VideoBlogComment, VideoBlogItem
from contacts.models import ContactInfo


def blog(request):
    article1 = Article()
    article1.isPhotoArticle = True
    article1.img = "img1.jpg"
    article1.imgTitle = "Apple Devices"
    article1.imgAltText = "Apple Devices"
    article1.headline = "The next generation of Multi-Touch"
    article1.date = "07.01.2017"
    article1.desc = "The original iPhone introduced the world to Multi-Touch, forever changing the way people experience technology. With 3D Touch, you can do things that were never possible before. It senses how deeply you press the display, letting you do all kinds of essential things more quickly and simply. And it gives you real-time feedback in the form of subtle taps from the all-new Taptic Engine."

    article2 = Article()
    article2.isVideoArticle = True
    article2.img = "img2.jpg"
    article2.imgTitle = "Coffee"
    article2.imgAltText = "Coffee"
    article2.headline = "MacBook Pro - brand new day for business"
    article2.date = "02.01.2017"
    article2.desc = "Organizations everywhere are realizing the potential that Mac brings to their employees by giving them the freedom to use the tools they already know and love. Software and hardware made for each other. Because Apple designs both the software and hardware, every Mac delivers the best possible experience for employees."

    article3 = Article()
    article3.isReviewArticle = True
    article3.img = "img4.jpg"
    article3.imgTitle = "HP Chromebook"
    article3.imgAltText = "HP Chromebook"
    article3.headline = "HP Chromebook review."
    article3.date = "02.01.2017"
    article3.desc = "HP’s Chromebook 11 G4 ($199) has a dull-gray shell that screams, “bulk education purchase” more than “buy me.” Precisely because this school-oriented model can bang around in backpacks, however, it could teach its consumer Chromebook cousins a thing or two about build quality."

    articles = [article1, article2, article3]

    contactInfo = ContactInfo()
    contactInfo.companyName = "FlyBuy, Inc."
    contactInfo.addressText1 = "1305 Market Street, Suite 800"
    contactInfo.addressText2 = "San Francisco, CA 94102"
    contactInfo.phoneNo = " (123) 456-7890"
    contactInfo.supportMail = "sup@example.com"
    contactInfo.partnerMail = "col@example.com"

    return render(request, 'blog/blog.html', {'articles': articles, 'contactInfo': contactInfo})


def item_photo(request):

    photoBlogItem = PhotoBlogItem()
    photoBlogItem.img = "item-photo.jpg"
    photoBlogItem.imgAltText = "Apple 3D Touch"
    photoBlogItem.headline = "Apple Introduces 3D Touch, The Next Generation Of Multitouch For The iPhone 6S"
    photoBlogItem.bodyText = "In an effort to deliver the next generation of what Apple CEO Tim Cook called \"the most-loved phone in the world,\" the iPhone 6S has created the next generation of its industry-shattering multitouch screen: the 3D Touch, which Chief Design Officer Jony Ive called \"a tremendous breakthrough in interacting with our devices\" in the company's demo video. \n \n Deemed \"a whole new dimension to the way you experience your iPhone\" by Apple, 3D Touch recognizes a user's wanted action via finger pressure and force, rather than a mere gesture like the traditional swipe or pinch. \n \n But how exactly does this work? The explanation is somewhat simple, even if the technology is more extensive than meets the eye. To wit: sensors within the smartphone measure the force of finger pressure, which then translates, letting the iPhone know the users needs and wants. \n \n For example, if a user applies a light pressure to the screen when selecting an option to view content, the preview for said content pops up; if the user presses harder on the option for the content, it will open automatically. \n \n Apple's Craig Federighi, senior vice president of software engineering, who conducted a live demo at the Apple event, also demonstrated how the new interactive interface eliminates going \"in and out\" of windows in certain apps, like mail apps – with 3D Touch, pressure dictates whether the user wants a sneak peek of a message, or to fully view it."

    pbc1 = PhotoBlogComment()
    pbc1.authorName = "Anne Hathaway"
    pbc1.date = "2 years ago"
    pbc1.comment = "Apple Music brings iTunes music streaming to the UK. But is it worth paying for? In our Apple Music review, we examine the service's features, UK pricing, audio quality and music library."

    pbc2 = PhotoBlogComment()
    pbc2.authorName = "Anne Hathaway"
    pbc2.date = "Today"
    pbc2.comment = "Apple Music brings iTunes music streaming to the UK. But is it worth paying for? In our Apple Music review, we examine the service's features, UK pricing, audio quality and music library."

    pbcs = [pbc1, pbc2]

    contactInfo = ContactInfo()
    contactInfo.companyName = "FlyBuy, Inc."
    contactInfo.addressText1 = "1305 Market Street, Suite 800"
    contactInfo.addressText2 = "San Francisco, CA 94102"
    contactInfo.phoneNo = " (123) 456-7890"
    contactInfo.supportMail = "sup@example.com"
    contactInfo.partnerMail = "col@example.com"

    return render(request, 'blog/item-photo.html', {'photoBlogItem': photoBlogItem, 'pbcs': pbcs, 'contactInfo': contactInfo})


def item_video(request):

    videoBlogItem = VideoBlogItem()
    videoBlogItem.id = "uf7U3Y2DFCA"
    videoBlogItem.title = "MacBook Pro - brand new day for business"
    videoBlogItem.desc = "So capable, you won’t want to put it down. So thin and light, you won’t have to."
    videoBlogItem.thumbImg = "item-video.jpg"
    videoBlogItem.thumbImgAltText = "MacBook Pro"
    videoBlogItem.headline = "MacBook Pro \n brand new day for business"
    videoBlogItem.bodyText = "Organizations everywhere are realizing the potential that Mac brings to their employees by giving them the freedom to use the tools they already know and love. \n \n Software and hardware made for each other. Because Apple designs both the software and hardware, every Mac delivers the best possible experience for employees. OS X works seamlessly with hardware in every Mac, like the super-responsive trackpad in Mac notebooks that make Multi-Touch gestures feel natural to use. And thanks to multicore Intel processors and fast flash storage, a Mac wakes instantly from sleep, ready to perform any task. \n \n New ways for employees to get work done. With OS X and the built-in apps that come with every Mac, employees can be productive right away — on a platform they love. And with innovative new types of business apps, employees are able to collaborate in new ways and manage their work like never before."

    vbc1 = VideoBlogComment()
    vbc1.authorName = "Anne Hathaway"
    vbc1.date = "2 years ago"
    vbc1.comment = "Apple Music brings iTunes music streaming to the UK. But is it worth paying for? In our Apple Music review, we examine the service's features, UK pricing, audio quality and music library"

    vbc2 = VideoBlogComment()
    vbc2.authorName = "Chris Hemsworth"
    vbc2.date = "Today"
    vbc2.comment = "Samsung's Galaxy S7 smartphone is getting serious hype. Here's what it does better than Apple's iPhone 6s."

    vbcs = [vbc1, vbc2]

    contactInfo = ContactInfo()
    contactInfo.companyName = "FlyBuy, Inc."
    contactInfo.addressText1 = "1305 Market Street, Suite 800"
    contactInfo.addressText2 = "San Francisco, CA 94102"
    contactInfo.phoneNo = " (123) 456-7890"
    contactInfo.supportMail = "sup@example.com"
    contactInfo.partnerMail = "col@example.com"

    return render(request, 'blog/item-video.html', {'videoBlogItem': videoBlogItem,  'vbcs': vbcs, 'contactInfo': contactInfo})


def item_review(request):

    reviewBlogItem = ReviewBlogItem()
    reviewBlogItem.title = "HP Chromebook laptops"
    reviewBlogItem.titleDesc = "With the HP Chromebook running lightning-fast Chrome OS,\nthe best of Google is at hand on a colorfully sleek and stylish notebook."
    reviewBlogItem.isVideoAvailable = True
    reviewBlogItem.videoId = "AqUjIs0pw_U"
    reviewBlogItem.thumbImg = "item-review.jpg"
    reviewBlogItem.thumbImgAltText = "HP Chromebook"
    reviewBlogItem.videoTitle = "HP Chromebook review"
    reviewBlogItem.videoDesc = "Detailed unboxing and review of the new Google designed 11-inch HP Chromebook. 239$"
    reviewBlogItem.startingPrice = 199.99
    reviewBlogItem.ffFlag = True
    reviewBlogItem.ffTitle1 = "Anywhere, anytime mobility."
    reviewBlogItem.ffTitle2 = "Fast, simple, secure."
    reviewBlogItem.ffImg = "review-2.jpg"
    reviewBlogItem.ffImgAltText = "500x500"
    reviewBlogItem.ffDesc = "School, home, or on the road, the slim design, and latest Intel® processor give you everything you need to take on the world.\nConveniently store up to 100GB of your files and content with the included 2-years of Google Drive access.\nWith up to 9.5 hours of long lasting battery, search, stream, chat, and more for hours without recharging."
    reviewBlogItem.sfFlag = True
    reviewBlogItem.sfTitle1 = "Entertainment at your fingertips."
    reviewBlogItem.sfTitle2 = "HP TrueVision."
    reviewBlogItem.sfImg = "review-1.jpg"
    reviewBlogItem.sfImgAltText = "500x500"
    reviewBlogItem.sfDesc = "Capture all the details with vibrant clarity, even in low light. Enjoy the nuances of face-to-face conversations, thanks to the HP TrueVision HD Webcam.\nLay back and get comfortable with your favorite movies and shows. The 11.6-inch diagonal HD IPS screen (optional) delivers your entertainment in stunning quality, from any angle"
    reviewBlogItem.thFlag = True
    reviewBlogItem.tfTitle1 = "Sleek and colorful."
    reviewBlogItem.tfTitle2 = "Checkmate."
    reviewBlogItem.tfImg = "review-3.jpg"
    reviewBlogItem.tfImgAltText = "500x500"
    reviewBlogItem.tfDesc = "With the HP Chromebook running lightning-fast Chrome OS, the best of Google is at hand on a colorfully sleek and stylish notebook. \n Express yourself with an HD 29.5 cm (11.6\") diagonal screen in a slim package, styled in smoke silver or sky blue."
    reviewBlogItem.bottomHeadline = "The stylish HP Chromebook provides \n a speedy connection to your protected online content and \n automatically updated apps"
    reviewBlogItem.bottomText = "All within an ultra-thin full-sized notebook, providing a comfortable gateway to surf, socialize and play."

    rProduct1 = ReviewProduct()
    rProduct1.isFavorite = True
    rProduct1.img = "chrome-book-11.jpg"
    rProduct1.imgAltText = "HP Chromebook 11"
    rProduct1.title = "HP Chromebook 11"
    rProduct1.sale = "199.99"
    rProduct1.label = "Laptops"

    rProduct2 = ReviewProduct()
    rProduct2.isFavorite = False
    rProduct2.img = "chrome-book-14.jpg"
    rProduct2.imgAltText = "HP Chromebook 14"
    rProduct2.title = "HP Chromebook 14"
    rProduct2.sale = 209.99
    rProduct2.isOffer = True
    rProduct2.priceThrough = 249.99
    rProduct2.label = "Laptops"

    rProducts = [rProduct1, rProduct2]

    contactInfo = ContactInfo()
    contactInfo.companyName = "FlyBuy, Inc."
    contactInfo.addressText1 = "1305 Market Street, Suite 800"
    contactInfo.addressText2 = "San Francisco, CA 94102"
    contactInfo.phoneNo = " (123) 456-7890"
    contactInfo.supportMail = "sup@example.com"
    contactInfo.partnerMail = "col@example.com"

    return render(request, 'blog/item-review.html', {'reviewBlogItem': reviewBlogItem, 'rProducts': rProducts, 'contactInfo': contactInfo})
