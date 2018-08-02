from django.db import models
from datetime import datetime
from django.conf import settings


class Project(models.Model):
    name = models.CharField(max_length=20)
    project_name = models.CharField(max_length=40)
    created_dt = models.DateTimeField(default=datetime.now(), blank=True)
    min_gpa = models.CharField(max_length=4)
    min_year = models.CharField(max_length=12)
    min_exp = models.CharField(max_length=2)
    kwords = models.TextField()
    req_classes = models.TextField()

    def __str__(self):
        return '<Name: {}, Project: {}, Created Date: {}, MinGPA: {}, MinYear: {}, MinExp: {}, Keywords: {}, ReqClasses: {}>'.format(
            self.name, self.project_name, self.created_dt, self.min_gpa, self.min_year, self.min_exp, self.kwords, self.req_classes)

class Applicant(models.Model):
	name = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
	project = models.ForeignKey(Project, default=1, on_delete=models.CASCADE)
	score = models.CharField(max_length=10, blank=True)

	def __str__(self):
		return '<Name: {}, Project: {}, Score: {}>'.format(self.name, self.project, self.score)