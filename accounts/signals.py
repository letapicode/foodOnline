"""
This code is a part of a Django project, which is a type of website that allows people to create, edit, and view information stored in a database. The code has two functions that are called when certain events happen in the website.

The first function is called post_save_profile_receiver. This function is called when a user's information is saved in the database, either because the user is being created for the first time or because their information is being updated.

The second function is called pre_save_profile_receiver. This function is called just before a user's information is saved in the database.

Both of these functions have something called a "decorator" above them, which is a special kind of function that helps them work with Django. The decorators are called @receiver, and they tell Django to run the functions when certain signals are sent.

The first function is called when a post_save signal is sent, and the second function is called when a pre_save signal is sent. These signals are sent by Django when a user's information is saved in the database.

Inside each function, there are some lines of code that do different things. For example, the first function checks if the user is being created for the first time, and if they are, it creates a new UserProfile for them. If the user already exists, the function tries to find their UserProfile and save it. If the UserProfile doesn't exist, the function creates one.

The second function just prints a message with the user's username and tells us that the user is being saved.

"""
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import User, UserProfile

# @receiver(post_save, sender=User)
# def post_save_profile_reveiver(sender, instance, created, **kwargs):
#     print(created)
#     if created:
#         UserProfile.objects.create(user=instance)
#     else:
#         try:
#             profile = UserProfile.objects.get(user=instance)
#             profile.save()
#         except:
#             #create the userprofile if not exit
#             UserProfile.objects.create(user=instance)


@receiver(pre_save, sender=User)
def pre_save_profile_receiver(sender, instance, **kwargs):
    pass

#post_save.connnect(post_save_create_profile_receiver, sender=User)

