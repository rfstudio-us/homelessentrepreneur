# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.admin import AdminSite
from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .models import Donations, Facilities, UserProfile,  location_history, short_survey_form, Job

admin.site.register(UserProfile,SimpleHistoryAdmin)
admin.site.register({Donations, Facilities, location_history, short_survey_form, Job})
# Register your models here.
