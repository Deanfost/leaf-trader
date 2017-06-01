
from django.contrib import admin

# Register your models here.

from finpy.models import Stock

admin.site.register(Stock)
