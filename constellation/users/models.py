from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    STUDENT = 1
    TEACHER = 2
    ROLE_CHOICES = (
        (STUDENT, 'Student'),
        (TEACHER, 'Teacher'),
    )
    FRESHMAN = 1
    SOPHOMORE = 2
    JUNIOR = 3
    SENIOR = 4
    YEAR_CHOICES = (
        (FRESHMAN, 'Freshman'),
        (SOPHOMORE, 'Sophomore'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gpa = models.CharField(max_length=4, blank=True)
    year = models.PositiveSmallIntegerField(choices=YEAR_CHOICES, null=True, blank=True)
    desc = models.TextField(max_length=300, blank=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, null=True, blank=True)

    def __str__(self): 
        return self.user.username

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

class Experience(models.Model):
    name = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    title = models.CharField(max_length=40, blank=True)
    company = models.CharField(max_length=40, blank=True)
    desc = models.TextField(max_length=200, null=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return '<Name: {}, Title: {}, Company: {}, Start Date: {}, End Date: {}, Desc: {}>'.format(self.name, self.title, self.company, self.start_date, self.end_date, self.desc)