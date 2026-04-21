from django.contrib import admin
from .models import Management, Leadership
from django.utils.html import format_html


@admin.register(Management)
class ManagementAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Main', {
            'fields': ('order',)
        }),
        ('Avatar', {
            'fields': ('avatar', 'avatar_preview')
        }),
        ('Fullname', {
            'fields': ('fullname_uz', 'fullname_ru', 'fullname_en')
        }),
        ('Position', {
            'fields': ('position_uz', 'position_ru', 'position_en')
        }),
        ('Contact', {
            'fields': ('phone', 'email')
        }),
    )
    ordering = ('order',)
    list_display = ('order', 'preview', 'fullname_uz', 'position_uz', 'phone', 'email')
    list_display_links = ('fullname_uz',)

    def preview(self, obj):
        if obj.avatar:
            return format_html(
                '<img src="{}" width="50" height="50" style="border-radius:50%;" />',
                obj.avatar.url
            )
        return "-"

    readonly_fields = ('avatar_preview',)

    def avatar_preview(self, obj):
        if obj and obj.avatar:
            return format_html(
                '<img src="{}" width="150" />',
                obj.avatar.url
            )
        return "No Image"


@admin.register(Leadership)
class LeadershipAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Main', {
            'fields': ('order',)
        }),
        ('Avatar', {
            'fields': ('avatar', 'avatar_preview')
        }),
        ('Fullname', {
            'fields': ('fullname_uz', 'fullname_ru', 'fullname_en')
        }),
        ('Position', {
            'fields': ('position_uz', 'position_ru', 'position_en')
        }),
        ('Contact', {
            'fields': ('phone', 'email')
        }),
    )
    ordering = ('order',)
    list_display = ('order', 'preview', 'fullname_uz', 'position_uz', 'phone', 'email')
    list_display_links = ('fullname_uz',)

    def preview(self, obj):
        if obj.avatar:
            return format_html(
                '<img src="{}" width="50" height="50" style="border-radius:50%;" />',
                obj.avatar.url
            )
        return "-"

    readonly_fields = ('avatar_preview',)

    def avatar_preview(self, obj):
        if obj and obj.avatar:
            return format_html(
                '<img src="{}" width="150" />',
                obj.avatar.url
            )
        return "No Image"
