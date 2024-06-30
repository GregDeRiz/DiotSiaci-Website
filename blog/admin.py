from django.contrib import admin
from .models import Article
from parler.admin import TranslatableAdmin


# Register your models here.
admin.site.register(Article, TranslatableAdmin)
