from django import forms


class TweetForm(forms.Form):
    your_tweet = forms.CharField(widget=forms.Textarea, label='Treść!', max_length=140)