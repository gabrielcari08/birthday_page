from django.contrib import admin
from .models import Card


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ['id', 'thumbnail', 'user', 'text_preview', 'created_at']
    list_filter = ['user', 'created_at']
    search_fields = ['text']
    list_per_page = 10
    readonly_fields = ['created_at']

    def thumbnail(self, obj):
        from django.utils.html import format_html
        return format_html('<img src="{}" width="50" height="50" style="object-fit: cover; border-radius: 5px;">', obj.image.url)
    thumbnail.short_description = 'Imagen'

    def text_preview(self, obj):
        return obj.text[:50] + '...' if len(obj.text) > 50 else obj.text
    text_preview.short_description = 'Texto'
