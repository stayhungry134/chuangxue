from django.contrib import admin

from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('art_author', 'art_title', 'art_body', 'article_label', 'art_created_time')
    list_filter = ('art_author', 'article_label')
    search_fields = ('art_author', 'art_title', 'article_label')
    fieldsets = (
        ('文章信息', {
            'fields': (
                ('article_label', 'art_author'),
            )
        }),
        ('文章内容', {
            'fields': (
                ('art_title', 'art_body')
            )
        }),
    )
