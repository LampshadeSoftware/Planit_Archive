from django.shortcuts import render
from .models import Section, WishList


# Create your views here.
def home(request):
	if request.POST:
		return render(request, 'boot.html', {'sections': {}})

	sections = {}
	subject = request.GET.get('term_subj', None)
	course_id = request.GET.get('course_id', None)
	if subject:  # if we got a valid GET request
		sections = Section.objects.all()

		# deals with getting a specified subject
		if subject != "0":
			sections = sections.filter(subject=subject)

		# deals with getting a specified course_id
		if course_id != "":
			sections = sections.filter(course_id=course_id)

		# gets rid of repeats
		already_added = set()
		no_repeats = []
		for section in sections:
			if section.title not in already_added:
				no_repeats.append({"subject": section.subject, "course_id": section.course_id, "title": section.title})
			already_added.add(section.title)

		# sends the response
		return render(request, 'boot.html', {'sections': no_repeats})
	else:
		return render(request, 'boot.html', sections)
