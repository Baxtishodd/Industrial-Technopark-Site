from django.db import models
from django.utils.translation import get_language
import uuid
from datetime import datetime
import os


def management_upload_path(instance, filename):
    ext = filename.split('.')[-1]
    today = datetime.now().strftime("%Y/%m/%d")
    return f"management/{today}/{uuid.uuid4()}.{ext}"


class Management(models.Model):
    avatar = models.ImageField(upload_to=management_upload_path)

    fullname_uz = models.CharField(max_length=255)
    fullname_ru = models.CharField(max_length=255)
    fullname_en = models.CharField(max_length=255)

    position_uz = models.CharField(max_length=255)
    position_ru = models.CharField(max_length=255)
    position_en = models.CharField(max_length=255)

    phone = models.CharField(max_length=20)
    email = models.EmailField()

    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.fullname_uz

    def get_fullname(self):
        lang = get_language()

        if lang == 'ru':
            return self.fullname_ru
        elif lang == 'en':
            return self.fullname_en
        return self.fullname_uz

    def get_position(self):
        lang = get_language()

        if lang == 'ru':
            return self.position_ru
        elif lang == 'en':
            return self.position_en
        return self.position_uz


def leadership_upload_path(instance, filename):
    ext = filename.split('.')[-1]
    today = datetime.now().strftime("%Y/%m/%d")
    return f"leadership/{today}/{uuid.uuid4()}.{ext}"


class Leadership(models.Model):
    avatar = models.ImageField(upload_to=leadership_upload_path)

    fullname_uz = models.CharField(max_length=255)
    fullname_ru = models.CharField(max_length=255)
    fullname_en = models.CharField(max_length=255)

    position_uz = models.CharField(max_length=255)
    position_ru = models.CharField(max_length=255)
    position_en = models.CharField(max_length=255)

    phone = models.CharField(max_length=20)
    email = models.EmailField()

    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.fullname_uz

    def get_fullname(self):
        lang = get_language()

        if lang == 'ru':
            return self.fullname_ru
        elif lang == 'en':
            return self.fullname_en
        return self.fullname_uz

    def get_position(self):
        lang = get_language()

        if lang == 'ru':
            return self.position_ru
        elif lang == 'en':
            return self.position_en
        return self.position_uz

















