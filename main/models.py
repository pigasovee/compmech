# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Menu(models.Model):
    title = models.CharField(default="", max_length=100, verbose_name="Заголовок")

    def __str__(self):
        return u"{}".format(self.title)

    def __unicode__(self):
        return u"{}".format(self.title)


class MenuItem(models.Model):
    title = models.CharField(default="", max_length=256, verbose_name="Заголовок")
    url = models.CharField(default="", max_length=256, verbose_name="URL")
    menu = models.ForeignKey(Menu, verbose_name="Меню")
    parent_item = models.ForeignKey('MenuItem', verbose_name="Родительский элемент", blank=True, null=True)
    weight = models.IntegerField(verbose_name="Вес", default=0)

    def __str__(self):
        return u"{}".format(self.title)

    def __unicode__(self):
        return u"{}".format(self.title)


class StaticPage(models.Model):
    title = models.CharField(default="", max_length=256, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Контент")
    published = models.BooleanField(default="False", verbose_name="Опубликовано")
    add_to = models.ManyToManyField(MenuItem, verbose_name="Добавить в...")

    def __str__(self):
        return u"{}".format(self.title)

    def __unicode__(self):
        return u"{}".format(self.title)


class StaffCategory(models.Model):
    name = models.CharField(default="", max_length=30)
    title = models.CharField(max_length=50)

    def __str__(self):
        return u"{}".format(self.title)

    def __unicode__(self):
        return u"{}".format(self.title)


class Staff(models.Model):
    staff_category = models.ForeignKey(StaffCategory, verbose_name="Категория")
    available = models.BooleanField(default="True", verbose_name="Действующий")
    ac_degree = models.CharField(max_length=100, verbose_name="Ученая степень")
    ac_title = models.CharField(max_length=100, verbose_name="Ученое звание")
    education = models.CharField(max_length=100, verbose_name="Направление подготовки (специальность)")
    work_start_date = models.DateField(null=True, verbose_name="Начало работы")
    work_spec_start_date = models.DateField(null=True, verbose_name="Начало работы по специальности")
    training = models.CharField(max_length=200, verbose_name="Повышение квалификации")
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return u"{} {} {}".format(self.staff_category, self.user.first_name, self.user.last_name)

    def __unicode__(self):
        return u"{} {} {}".format(self.staff_category, self.user.first_name, self.user.last_name)


class Discipline(models.Model):
    title = models.CharField(max_length=100)
    educator = models.ManyToManyField(Staff)

    def __str__(self):
        return u"{} {} {}".format(self.staff_category, self.user.first_name, self.user.last_name)

    def __unicode__(self):
        return u"{} {} {}".format(self.staff_category, self.user.first_name, self.user.last_name)


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Контент")
    images = models.ImageField(blank=True)
    files = models.FileField(blank=True)
    published = models.BooleanField(default="False", verbose_name="Опубликовано")
    add_to = models.ManyToManyField(MenuItem, verbose_name="Добавить в...")

    def __str__(self):
        return u"{}".format(self.title)

    def __unicode__(self):
        return u"{}".format(self.title)


class Photo(models.Model):
    post = models.ForeignKey(Post)
    image = models.ImageField(upload_to='photos')
    caption = models.CharField(max_length=100, blank=True)
