from django.contrib import admin

from blog.models import Category, Comment, Newsletter, Post, Author

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Newsletter)
admin.site.register(Author)
