from django.db import models


class Content(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    page_slug = models.CharField(max_length=200)
    pub_date = models.DateField('date published')
    meta_title = models.CharField(max_length=200)
    meta_description = models.CharField(max_length=500)
    is_menu = models.BooleanField()

    def __unicode__(self):
        return self.title


class Images(models.Model):
    content = models.ForeignKey(Content)
    alt = models.CharField(max_length=200)
    url = models.ImageField(upload_to='contents/static/images')

    def __unicode__(self):
        return self.alt


class slideshow(models.Model):
    content = models.ForeignKey(Content)
    alt = models.CharField(max_length=200)
    url = models.ImageField(upload_to='contents/static/slideshows')

    def __unicode__(self):
        return self.alt


from django import forms


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'cols': 40}))
    sender = forms.EmailField()
    name = forms.CharField(max_length=100)
    cc_myself = forms.BooleanField(required=False)