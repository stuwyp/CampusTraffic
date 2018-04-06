# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import admin_td, Car_td, Vister_td, carareanum, CardataApril,CardataAugust,CardataDecember, CardataFebruary, CardataJanuary 

admin.site.register(Vister_td)
admin.site.register(admin_td)
admin.site.register(carareanum)
admin.site.register(CardataApril)
admin.site.register(CardataAugust)


class AuthorAdmin(admin.ModelAdmin):
     search_fields = ('carnum',)

admin.site.register(Car_td,AuthorAdmin)
