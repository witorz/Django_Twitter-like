# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views import View
from django.shortcuts import render
from .models import Tweet
from .forms import TweetForm


class MainView(View):
    def get(self, request):
        return render(request, 'twitter/index.html')


class TweetView(View):
    def get(self, request):
        x = Tweet.objects.all()
        return render(request, 'twitter/tweets.html', {'tweets': x})


class LoggedOutView(View):
    def get(self, request):
        return render(request, 'registration/logged_out.html')


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TweetForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            dane = form.cleaned_data['your_tweet']
            forms = Tweet.objects.save(content=dane)
            return render(request, 'twitter/tweets.html', {'form': forms})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = TweetForm()
        return render(request, 'twitter/tweets.html', {'form': form})