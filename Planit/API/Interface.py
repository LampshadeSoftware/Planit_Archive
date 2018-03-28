

import os
import sys

import django

sys.path.append('..')
# you have to set the correct path to you settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Planit.Planit.settings")

django.setup()

from API.User import *

# your imports, e.g. Django models
from courses_database.models import WishList

from API.Section import *
from API.TimeBlock import *


'''
wish_list should be a list of dictionaries where each dictionary has
subject, course_id, and title as keys
'''
def compute_schedules(wish_list, filters):
	user = API_User()

	for course in wish_list:
		user.add_to_wish_list(str(course['subject']), str(course['course_id']))

	for filter in filters:
		# apply filter
		pass

	# apply filters
	"""
	for x in user.get_all_schedules():
		print("NEW SCHEDULE")
		print(x)
		print()
	"""

	#print(user.get_all_schedules_as_dict())
	return user.get_all_schedules_as_dict()

