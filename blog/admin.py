from django.contrib import admin
from blog.models import Article, PhotoBlogItem, PhotoBlogComment, VideoBlogItem, VideoBlogComment, ReviewBlogItem, ReviewProduct

# Register your models here.
admin.site.register(Article)
admin.site.register(PhotoBlogItem)
admin.site.register(PhotoBlogComment)
admin.site.register(VideoBlogItem)
admin.site.register(VideoBlogComment)
admin.site.register(ReviewBlogItem)
admin.site.register(ReviewProduct)
