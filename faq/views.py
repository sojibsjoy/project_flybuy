from faq.models import LeftQuestion, RightQuestion
from contacts.models import ContactInfo
from django.shortcuts import render


def faq(request):

    leftQ1 = LeftQuestion()
    leftQ1.qId = "leftQ1"
    leftQ1.qText = "11How much should I bid?"
    leftQ1.qAnswer = "FlyBuy is great for finding deals, as long as you know what you're looking for and how much the item is worth. Having that information is vital to placing bids in correct amount and saving lots of money."

    leftQ2 = LeftQuestion()
    leftQ2.qId = "leftQ2"
    leftQ2.qText = "22How much should I bid?"
    leftQ2.qAnswer = "FlyBuy is great for finding deals, as long as you know what you're looking for and how much the item is worth. Having that information is vital to placing bids in correct amount and saving lots of money."

    leftQ3 = LeftQuestion()
    leftQ3.qId = "leftQ3"
    leftQ3.qText = "33How much should I bid?"
    leftQ3.qAnswer = "FlyBuy is great for finding deals, as long as you know what you're looking for and how much the item is worth. Having that information is vital to placing bids in correct amount and saving lots of money."

    leftQ4 = LeftQuestion()
    leftQ4.qId = "leftQ4"
    leftQ4.qText = "44How much should I bid?"
    leftQ4.qAnswer = "FlyBuy is great for finding deals, as long as you know what you're looking for and how much the item is worth. Having that information is vital to placing bids in correct amount and saving lots of money."

    leftQs = [leftQ1, leftQ2, leftQ3, leftQ4]

    rightQ1 = RightQuestion()
    rightQ1.qId = "rightQ1"
    rightQ1.qText = "2211How much should I bid?"
    rightQ1.qAnswer = "FlyBuy is great for finding deals, as long as you know what you're looking for and how much the item is worth. Having that information is vital to placing bids in correct amount and saving lots of money."

    rightQ2 = RightQuestion()
    rightQ2.qId = "rightQ2"
    rightQ2.qText = "2222How much should I bid?"
    rightQ2.qAnswer = "FlyBuy is great for finding deals, as long as you know what you're looking for and how much the item is worth. Having that information is vital to placing bids in correct amount and saving lots of money."

    rightQ3 = RightQuestion()
    rightQ3.qId = "rightQ3"
    rightQ3.qText = "2233How much should I bid?"
    rightQ3.qAnswer = "FlyBuy is great for finding deals, as long as you know what you're looking for and how much the item is worth. Having that information is vital to placing bids in correct amount and saving lots of money."

    rightQ4 = RightQuestion()
    rightQ4.qId = "rightQ4"
    rightQ4.qText = "2244How much should I bid?"
    rightQ4.qAnswer = "FlyBuy is great for finding deals, as long as you know what you're looking for and how much the item is worth. Having that information is vital to placing bids in correct amount and saving lots of money."

    rightQs = [rightQ1, rightQ2, rightQ3, rightQ4]

    contactInfo = ContactInfo()
    contactInfo.companyName = "FlyBuy, Inc."
    contactInfo.addressText1 = "1305 Market Street, Suite 800"
    contactInfo.addressText2 = "San Francisco, CA 94102"
    contactInfo.phoneNo = " (123) 456-7890"
    contactInfo.supportMail = "sup@example.com"
    contactInfo.partnerMail = "col@example.com"

    return render(request, 'faq/faq.html', {'leftQs': leftQs, 'rightQs': rightQs, 'contactInfo': contactInfo})
