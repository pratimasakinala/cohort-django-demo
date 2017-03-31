from django.contrib import admin

from .models import Post, Comment

class CommentInLine(admin.StackedInline):
    model = Comment

class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    list_display = ['title', 'created_at', 'status', 'author']
    list_filter = ['status', 'created_at', 'author']
    inlines = [CommentInLine]

admin.site.register(Post, PostAdmin)
