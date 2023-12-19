from django.contrib import admin

# Register your models here.
from .models import Post, Comments

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('tittle', 'author')

@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('name', 'post')
