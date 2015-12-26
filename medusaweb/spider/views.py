#!/usr/bin/env python
# coding: utf-8

import datetime
import random

from django.conf import settings
from django.http import HttpResponse
from django.template import Template,Context
from django.template.loader import get_template
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.views.generic import View
from django.core.urlresolvers import reverse
from django.core.files.uploadedfile import UploadedFile, InMemoryUploadedFile, TemporaryUploadedFile
from django.core.files import File
from django.core.files.images import ImageFile


from coffin.shortcuts import render as coffin_render
class Jinja2View(View):
    """
    使用 Jinja2 模板
    """
    def get(self, request, *args, **kwargs):
        context = {}
        print '------------------------------------------------------------'
        context.update(coffin_version='0.4.0')
        context.update(none_value=None)
        print context
        # {'coffin_version': '0.4.0', 'none_value': None}
        """
        跟 Django 模板不同，Jinja2 模板会将 None 显示为字符串 "None"
        """
        print '------------------------------------------------------------'
        return coffin_render(request, 'jinja2.html', context)
