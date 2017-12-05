# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Menu, MenuItem, StaticPage, Staff, StaffCategory, Discipline, Post, Photo
from django.contrib import admin


admin.site.register(Menu)
admin.site.register(MenuItem)
admin.site.register(StaticPage)
admin.site.register(Staff)
admin.site.register(StaffCategory)
admin.site.register(Discipline)
admin.site.register(Post)
admin.site.register(Photo)
