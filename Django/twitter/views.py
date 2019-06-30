# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views import View
from django.shortcuts import render

class MainView(View):
    def get(self, request):
        return render(request, 'twitter/base.html')