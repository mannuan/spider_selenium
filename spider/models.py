# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.utils.six import python_2_unicode_compatible
from django.contrib.auth.models import User
import django.utils.timezone as timezone

@python_2_unicode_compatible
class Website(models.Model):
    name = models.CharField('网站来源', max_length=100)
    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Region(models.Model):
    name = models.CharField('景区', max_length=100)
    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Type(models.Model):
    name = models.CharField('数据类型', max_length=100)
    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Project(models.Model):
    project_id = models.AutoField('项目编号', primary_key=True)
    name = models.CharField('项目名称', max_length=200)
    status = models.CharField('项目状态', max_length=200, default='stop', editable=False)
    website = models.ForeignKey(Website)
    region = models.ForeignKey(Region)
    type = models.ForeignKey(Type)
    created_time = models.DateTimeField('首次创建时间', default = timezone.now, editable=False)
    modified_time = models.DateTimeField('最后修改时间', auto_now=True)
    editor = models.ForeignKey(User)
    def __str__(self):
        return str(self.project_id)