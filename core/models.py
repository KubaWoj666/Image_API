from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator

from django_advance_thumbnail import AdvanceThumbnailField

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from imagekit.models import ProcessedImageField

import uuid

from PIL import Image
from django.core.files import File
from tempfile import NamedTemporaryFile

User = settings.AUTH_USER_MODEL 


class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    account_tiers = models.ForeignKey("AccountTiers", on_delete=models.SET_NULL, null=True)

class AccountTiers(models.Model):
    name = models.CharField(max_length=20)
    thumbnail_size = models.ManyToManyField("ThumbnailsSize",  blank=True)
    original_image_link = models.BooleanField(default=False)
    expiring_link = models.BooleanField(default=False)
    class Mete:
        verbose_name_plural = "AccountTiers"

    def __str__(self) -> str:
        return self.name
    

class Images(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images", validators=[FileExtensionValidator(allowed_extensions=['png', 'jpeg'])])
    class Meta:
        verbose_name_plural = "Images"

    def __str__(self) -> str:
        return self.owner.username
    
    
class ThumbnailsSize(models.Model):
    width = models.PositiveIntegerField()
    height = models.PositiveIntegerField()
    class Mete:
        verbose_name_plural = "ThumbnailsSize"

    def __str__(self) -> str:
        return f"{self.width}x{self.height}"

  
class Thumbnail(models.Model):
    image = models.ForeignKey(Images, on_delete=models.CASCADE)
    thumbnail = models.ImageField(upload_to="source_image")
    thumbnail_200 = AdvanceThumbnailField(source_field="thumbnail", upload_to="thumbnail_200", null=True, blank=True, size=(200, 200))
    thumbnail_400 = AdvanceThumbnailField(source_field="thumbnail", upload_to="thumbnail_200", null=True, blank=True, size=(400, 400))

    
    

    