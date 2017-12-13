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
        'menu_1_items': MenuItem.objects.filter(menu__title='main1').order_by('weight'),
        'menu_2_items': MenuItem.objects.filter(menu__title='main2').order_by('weight'),
        'title': 'Hello World!'
    }
    return HttpResponse(template.render(context, request))


def page_view(request, url):
    current_page = MenuItem.objects.get(url=url)
    template = loader.get_template('main/menu_item_page.html')

    pages = StaticPage.objects.filter(published=True, add_to__exact=current_page.id)
    posts = Post.objects.filter(published=True, add_to__exact=current_page.id)

    context = {
        'title': current_page.title,
        'menu_1_items': MenuItem.objects.filter(menu__title='main1').order_by('weight'),
        'menu_2_items': MenuItem.objects.filter(menu__title='main2').order_by('weight'),
        'pages': pages,
        'posts': posts
    }
    return HttpResponse(template.render(context, request))
