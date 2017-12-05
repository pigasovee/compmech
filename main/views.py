# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Menu, MenuItem, Staff, StaffCategory, StaticPage, Post, Photo
from django.template import loader
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse


# Create your views here.
def homepage(request):
    template = loader.get_template('main/homepage.html')
    context = {
        'menu_items': MenuItem.objects.filter(menu__title='main'),
        'title': 'Hello World!'
    }
    return HttpResponse(template.render(context, request))
