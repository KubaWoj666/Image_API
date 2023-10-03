from django.contrib.auth.models import Group
from django.db.models.signals import post_migrate, post_save
from django.dispatch import receiver
from .models import Images

from PIL import Image as PILImage


@receiver(post_migrate)
def create_groups(sender, **kwargs):
    basic_group, created = Group.objects.get_or_create(name="Basic")
    premium_group, created = Group.objects.get_or_create(name="Premium")
    enterprise_group, created = Group.objects.get_or_create(name="Enterprise")


# @receiver(post_save, sender=Images)
# def generate_thumbnails(sender, instance, created, **kwargs):
#     if created:
#         img = PILImage.open(instance.image.path)

#         thumbnail_200 = img.copy()
#         thumbnail_200.thumbnail((200, 200))
#         thumbnail_200_path = f'thumbnail_200_{instance.id}.png'
#         thumbnail_200.save(thumbnail_200_path)
        
#         # Generate 400x400 thumbnail
#         thumbnail_400 = img.copy()
#         thumbnail_400.thumbnail((400, 400))
#         thumbnail_400_path = f'thumbnail_400_{instance.id}.png'
#         thumbnail_400.save(thumbnail_400_path)

#         Thumbnail.objects.create(images=instance, thumbnail_200=thumbnail_200_path, thumbnail_400=thumbnail_400_path)