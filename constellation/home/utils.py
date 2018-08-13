from .models import Project, Applicant
from django.contrib.auth.models import User
from users.models import Experience


def score(user, project):
	final_score = 0
	
	gpa = user.profile.gpa
	year = user.profile.year
	desc = user.profile.desc

	exps = Experience.objects.filter(name=user)
	scores = {}
	for idx, exp in enumerate(exps):
		scores[idx] = (exp.title + exp.company + exp.desc, exp.end_date - exp.start_date)


	
	
	return final_score