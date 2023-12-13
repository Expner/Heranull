from django import forms


class ImageLinkForm(forms.Form):
    imageLink = forms.CharField()