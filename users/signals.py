from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


# we are doing this because we want to create profile for each new user

@receiver(post_save,sender=User)
def create_Profile(sender,instance,created,**kwargs ):
	if created:
		Profile.objects.create(user=instance)

### whenver user is created the profile is created

@receiver(post_save,sender=User)
def save_Profile(sender,instance,**kwargs ):
	instance.profile.save()


## to save the profile