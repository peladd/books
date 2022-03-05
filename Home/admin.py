from django.contrib import admin

# Register your models here.
from Home.models import Post, Product, Profile, BlogPost


admin.site.register(Post)
admin.site.register(Product)
admin.site.register(Profile)
admin.site.register(BlogPost)