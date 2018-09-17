from .models import Project, Applicant
from django.contrib.auth.models import User
from users.models import Experience


def score(user, project):
	final_score = 0.0
	
	gpa = user.profile.gpa
	year = user.profile.year
	desc = user.profile.desc
	skills = user.profile.skills
	classes = user.profile.classes

	exps = Experience.objects.filter(name=user)
	scores = {}
	for idx, exp in enumerate(exps):
		scores[idx] = (exp.title + exp.company + exp.desc, exp.end_date - exp.start_date)

	#for val in scores.values:
		# count number of times kwords and project name in val[0] * 0.5
		# if greater than 0, += 2*val[1] - min_exp 

	# do the same for skills as done for experience...count number of times apeards in kewords and project name

	if project.min_gpa is not None and gpa is not None:
		final_score += 2*float(gpa) - float(project.min_gpa) * 10

	if project.min_year is not None and year is not None:
		final_score += 2*int(year) - int(project.min_year) * 10

	#if project.req_classes is not None and classes is not None:
	# count number of req_classes in classes and subtract from number not and 
	# multiply by 3
	
	return final_score