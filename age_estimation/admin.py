#! -*- coding: utf-8 -*-
from django.contrib import admin

from age_estimation.models import UserInfo, Learn

admin.site.register(UserInfo)
admin.site.register(Learn)
