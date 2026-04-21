from django.contrib import admin
from django.utils.html import format_html
from .models import News, Album, AlbumImage, Document


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Main', {
            'fields': ('category', 'published_at', 'image', 'image_preview')
        }),
        ('Title', {
            'fields': ('title_uz', 'title_ru', 'title_en')
        }),
        ('Body', {
            'fields': ('body_uz', 'body_ru', 'body_en')
        }),
    )
    ordering = ('-published_at',)
    list_display = ('preview', 'title_uz', 'category', 'published_at', 'views')
    list_display_links = ('title_uz',)
    list_filter = ('category',)
    search_fields = ('title_uz', 'title_ru', 'title_en')
    readonly_fields = ('image_preview', 'views')

    def preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="60" height="45" style="object-fit:cover; border-radius:4px;" />',
                obj.image.url
            )
        return "-"
    preview.short_description = 'Image'

    def image_preview(self, obj):
        if obj and obj.image:
            return format_html(
                '<img src="{}" width="300" style="border-radius:8px;" />',
                obj.image.url
            )
        return "No Image"
    image_preview.short_description = 'Preview'


# ─── GALLERY ───────────────────────────────────────────────

class AlbumImageInline(admin.TabularInline):
    model = AlbumImage
    extra = 3
    fields = ('image', 'preview', 'order')
    readonly_fields = ('preview',)

    def preview(self, obj):
        if obj and obj.image:
            return format_html(
                '<img src="{}" width="80" height="60" style="object-fit:cover; border-radius:4px;" />',
                obj.image.url
            )
        return "-"
    preview.short_description = 'Preview'


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Main', {
            'fields': ('published_at', 'cover', 'cover_preview')
        }),
        ('Title', {
            'fields': ('title_uz', 'title_ru', 'title_en')
        }),
    )
    inlines = [AlbumImageInline]
    ordering = ('-published_at',)
    list_display = ('cover_thumb', 'title_uz', 'published_at', 'image_count')
    list_display_links = ('title_uz',)
    search_fields = ('title_uz', 'title_ru', 'title_en')
    readonly_fields = ('cover_preview',)

    def cover_thumb(self, obj):
        if obj.cover:
            return format_html(
                '<img src="{}" width="60" height="45" style="object-fit:cover; border-radius:4px;" />',
                obj.cover.url
            )
        return "-"
    cover_thumb.short_description = 'Cover'

    def cover_preview(self, obj):
        if obj and obj.cover:
            return format_html(
                '<img src="{}" width="300" style="border-radius:8px;" />',
                obj.cover.url
            )
        return "No Image"
    cover_preview.short_description = 'Preview'

    def image_count(self, obj):
        return obj.images.count()
    image_count.short_description = 'Images'


# ─── DOCUMENT ──────────────────────────────────────────────

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Main', {
            'fields': ('category', 'published_at', 'file')
        }),
        ('Title', {
            'fields': ('title_uz', 'title_ru', 'title_en')
        }),
        ('Description', {
            'fields': ('description_uz', 'description_ru', 'description_en')
        }),
    )
    ordering = ('-published_at',)
    list_display = ('title_uz', 'category', 'published_at', 'file_ext')
    list_display_links = ('title_uz',)
    list_filter = ('category',)
    search_fields = ('title_uz', 'title_ru', 'title_en')

    def file_ext(self, obj):
        ext = obj.file_extension()
        colors = {'PDF': '#e74c3c', 'DOC': '#2980b9', 'DOCX': '#2980b9', 'XLS': '#27ae60', 'XLSX': '#27ae60'}
        color = colors.get(ext, '#7f8c8d')
        return format_html(
            '<span style="background:{};color:#fff;padding:2px 8px;border-radius:4px;font-size:11px;">{}</span>',
            color, ext
        )
    file_ext.short_description = 'Type'
