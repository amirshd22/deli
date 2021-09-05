from django.db.models.signals import post_save, pre_save, post_delete
from django.contrib.auth.models import User
from .models import Student


def create_student(sender, instance, created, **kwargs):
	if created:
		Student.objects.create(
			user=instance,
			#email=instance.email,
			)
            
		print('Student Created!')


post_save.connect(create_student, sender=User)
