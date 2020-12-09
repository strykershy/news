
# Create your models here.
from typing import ContextManager
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

class Article(models.Model):
    article_title = models.CharField(max_length=300)
    article_text = models.TextField()
    date_published = models.DateField('date published')
    def __str__(self):
        return self.article_title

class Category(models.Model):
    articles = models.ManyToManyField(Article)
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
