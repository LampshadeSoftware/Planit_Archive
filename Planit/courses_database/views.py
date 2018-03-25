from django.shortcuts import render
from .models import Section, WishList

import API.Interface as Interface

last_get = None


# Create your views here.
def home(request):
	global last_get


	if request.POST:
		wish_subject = request.GET.get('wish_subject', None)
		wish_course_id = request.GET.get('wish_course_id', None)
		new_wish_item = WishList()
		setattr(new_wish_item, "course_id", wish_course_id)
		setattr(new_wish_item, "subject", wish_subject)
		new_wish_item.save()
		request = last_get
	else:
		last_get = request

	wishlist = WishList.objects.all()
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
		sections = no_repeats

	index = 1
	if request.GET:
		index = request.GET.get("schedulenum", 1)

	schedules = Interface.compute_schedules()
	indices = [i + 1 for i in range(len(schedules))]
	schedule = []
	try:
		schedule = schedules[int(index) - 1]
	except:
		pass

	# sends the response
	return render(request, 'boot.html', {'sections': sections, "schedule": schedule, "num_schedules": len(schedules), "wishlist": wishlist, "indices": indices, "index": index})
