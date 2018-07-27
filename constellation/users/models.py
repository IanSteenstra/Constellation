from django.db import models
from django.conf import settings

# Create your models here.

class Experience(models.Model):
    name = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    title = models.CharField(max_length=40, blank=True)
    company = models.CharField(max_length=40, blank=True)
    desc = models.TextField(max_length=200, null=True)

    def __str__(self):
        return '<Name: {}, Title: {}, Company: {}, Desc: {}>'.format(self.name, self.title, self.company, self.desc)