from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    page_slug = models.CharField(max_length=200)

    def __unicode__(self):
        return self.title


class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    pub_date = models.DateField('date published')
    is_comment = models.BooleanField()
    category = models.ForeignKey(Category)
    page_slug = models.CharField(max_length=200)

    def __unicode__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(User)
    blog = models.ForeignKey(Blog)
    comment = models.TextField()


User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])

from cube.models import Cube, Dimension


class BlogCube(Cube):
    page_slug = Dimension('page_slug')
    title = Dimension('title')
    description = Dimension('description')
    pub_date = Dimension('pub_date')
    is_comment = Dimension('is_comment')

    @staticmethod
    def aggregation(queryset):
        return queryset.count()




