from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile,user

@receiver(post_save, sender=user)
def post_save_create_profile(sender, instance, created, **kwargs):
    #print('sender', sender)
    #print('instance', instance)
    #print(uid)
    if created:
        Profile.objects.create(Pr_id=instance)


