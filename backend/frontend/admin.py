from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('title', 'description')
    ordering = ('-created_at',)

admin.site.register(Article, ArticleAdmin)