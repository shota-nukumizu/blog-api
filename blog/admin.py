from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import ArticleModel, TagModel

class ArticleAdmin(MarkdownxModelAdmin):
    list_display = (
        'title',
        'get_tag',
        'slug',
        'is_public',
        'created_at'
    )
    list_display_links = list_display
    ordering = ('-created_at', )

    def get_tag(self, row):
        return ','.join([x.name for x in row.tag.all()])


class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'color')

admin.site.register(ArticleModel, ArticleAdmin)
admin.site.register(TagModel, TagAdmin)