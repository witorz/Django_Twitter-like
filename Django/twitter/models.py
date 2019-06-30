# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Tweet(models.Model):
    content = models.CharField(max_length=32)
    date = models.DateTimeField(default=datetime.now)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)