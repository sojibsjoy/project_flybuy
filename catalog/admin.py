from django.contrib import admin
from catalog.models import ProductItem, ProductDetail, Comment, PreviewItem

# Register your models here.
admin.site.register(ProductItem)
admin.site.register(ProductDetail)
admin.site.register(Comment)
admin.site.register(PreviewItem)
