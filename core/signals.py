from django.db.models.signals import post_migrate, post_save
from django.dispatch import receiver

from .models import AccountTiers, Images, Thumbnail, ThumbnailsSize

from PIL import Image

@receiver(post_migrate)
def default_account_tiers_create(sender, **kwargs):
    if sender.name == "core":
        thumbnail_200 = ThumbnailsSize.objects.create(width=200, height=200)
        thumbnail_400 = ThumbnailsSize.objects.create(width=400, height=400)


        Basic = AccountTiers.objects.create(name="Basic")
        Basic.thumbnail_size.set([thumbnail_200])
        Premium  = AccountTiers.objects.create(name="Premium", original_image_link=True)
        Premium.thumbnail_size.set([thumbnail_200, thumbnail_400])
        Enterprise = AccountTiers.objects.create(name="Enterprise", original_image_link=True, expiring_link=True)
        Enterprise.thumbnail_size.set([thumbnail_200, thumbnail_400])

        

@receiver(post_save, sender=Images)
def create_thumbnail(sender, created, instance, *args, **kwargs):
    if created:
        image = instance.image
        
        account_name = instance.owner.account_tiers
        account_tier = AccountTiers.objects.get(name=account_name)

        Thumbnail.objects.create(image=instance, thumbnail=image)

        qs_thumbnail_sizes = account_tier.thumbnail_size.all()

        for thumbnail_size in qs_thumbnail_sizes:
            width = thumbnail_size.width
            height = thumbnail_size.height

            image_obj = Images.objects.last()
            thumbnail_obj = Thumbnail.objects.last()
            if thumbnail_obj is not None:
                thumbnail_path = thumbnail_obj.thumbnail.path

            if image_obj is not None:
                image_path = image_obj.image.path
                
            im = Image.open(image_path)
            new_size = (width, height)
            im = im.resize(new_size)
            im.save(thumbnail_path)
    


        
