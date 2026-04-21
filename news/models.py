from django.db import models
from django.utils.translation import get_language
import uuid
from datetime import datetime


class NewsCategory(models.TextChoices):
    NEWS = 'news', 'News'
    EVENTS = 'events', 'Events'
    PRESS_RELEASE = 'press_release', 'Press-reliz'
    REPORTS = 'reports', 'Reports'


def news_upload_path(instance, filename):
    ext = filename.split('.')[-1]
    today = datetime.now().strftime("%Y/%m/%d")
    return f"news/{today}/{uuid.uuid4()}.{ext}"


class News(models.Model):
    category = models.CharField(
        max_length=20,
        choices=NewsCategory.choices,
        default=NewsCategory.NEWS
    )

    title_uz = models.CharField(max_length=255)
    title_ru = models.CharField(max_length=255)
    title_en = models.CharField(max_length=255)

    body_uz = models.TextField()
    body_ru = models.TextField()
    body_en = models.TextField()

    image = models.ImageField(upload_to=news_upload_path)

    published_at = models.DateField()
    views = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-published_at']
        verbose_name = 'News'
        verbose_name_plural = 'News'

    def __str__(self):
        return self.title_uz

    def get_title(self):
        lang = get_language()
        if lang == 'ru':
            return self.title_ru
        elif lang == 'en':
            return self.title_en
        return self.title_uz

    def get_body(self):
        lang = get_language()
        if lang == 'ru':
            return self.body_ru
        elif lang == 'en':
            return self.body_en
        return self.body_uz


# ─── GALLERY ───────────────────────────────────────────────

def album_cover_path(instance, filename):
    ext = filename.split('.')[-1]
    today = datetime.now().strftime("%Y/%m/%d")
    return f"gallery/covers/{today}/{uuid.uuid4()}.{ext}"


def album_image_path(instance, filename):
    ext = filename.split('.')[-1]
    today = datetime.now().strftime("%Y/%m/%d")
    return f"gallery/images/{today}/{uuid.uuid4()}.{ext}"


class Album(models.Model):
    title_uz = models.CharField(max_length=255)
    title_ru = models.CharField(max_length=255)
    title_en = models.CharField(max_length=255)

    cover = models.ImageField(upload_to=album_cover_path)
    published_at = models.DateField()

    class Meta:
        ordering = ['-published_at']
        verbose_name = 'Album'
        verbose_name_plural = 'Albums'

    def __str__(self):
        return self.title_uz

    def get_title(self):
        lang = get_language()
        if lang == 'ru':
            return self.title_ru
        elif lang == 'en':
            return self.title_en
        return self.title_uz

    def image_count(self):
        return self.images.count()


class AlbumImage(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to=album_image_path)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.album.title_uz} - {self.order}"


# ─── DOCUMENT ──────────────────────────────────────────────

class DocumentCategory(models.TextChoices):
    ORDER = 'order', 'Buyruqlar'
    REGULATION = 'regulation', 'Nizomlar'
    REPORT = 'report', 'Hisobotlar'
    OTHER = 'other', 'Boshqalar'


def document_upload_path(instance, filename):
    ext = filename.split('.')[-1]
    today = datetime.now().strftime("%Y/%m/%d")
    return f"documents/{today}/{uuid.uuid4()}.{ext}"


class Document(models.Model):
    category = models.CharField(
        max_length=20,
        choices=DocumentCategory.choices,
        default=DocumentCategory.OTHER
    )

    title_uz = models.CharField(max_length=255)
    title_ru = models.CharField(max_length=255)
    title_en = models.CharField(max_length=255)

    description_uz = models.TextField(blank=True)
    description_ru = models.TextField(blank=True)
    description_en = models.TextField(blank=True)

    file = models.FileField(upload_to=document_upload_path)
    published_at = models.DateField()

    class Meta:
        ordering = ['-published_at']
        verbose_name = 'Document'
        verbose_name_plural = 'Documents'

    def __str__(self):
        return self.title_uz

    def get_title(self):
        lang = get_language()
        if lang == 'ru':
            return self.title_ru
        elif lang == 'en':
            return self.title_en
        return self.title_uz

    def get_description(self):
        lang = get_language()
        if lang == 'ru':
            return self.description_ru
        elif lang == 'en':
            return self.description_en
        return self.description_uz

    def file_extension(self):
        name = self.file.name
        return name.split('.')[-1].upper() if '.' in name else 'FILE'
