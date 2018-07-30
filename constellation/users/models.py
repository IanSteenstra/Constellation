from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gpa = models.CharField(max_length=3, blank=True)
    year = models.CharField(max_length=30, blank=True)
    desc = models.TextField(max_length=300, blank=True)

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()

class Experience(models.Model):
    name = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    title = models.CharField(max_length=40, blank=True)
    company = models.CharField(max_length=40, blank=True)
    desc = models.TextField(max_length=200, null=True)
    time = models.CharField(max_length=4, blank=True)

    def __str__(self):
        return '<Name: {}, Title: {}, Company: {}, Time: {}, Desc: {}>'.format(self.name, self.title, self.company, self.time, self.desc)